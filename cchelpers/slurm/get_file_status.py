from tenacity import retry, stop_after_attempt, wait_random, wait_exponential, retry_if_exception_type, before_sleep_log
import time
import subprocess
import logging
from cchelpers.jobs import JobStatus
import os
import glob

logger = logging.getLogger(__name__)


@retry(stop=stop_after_attempt(5),
       wait=wait_random(min=1, max=2) +
       wait_exponential(multiplier=1, min=1, max=5),
       retry=retry_if_exception_type(subprocess.TimeoutExpired),
       before_sleep=before_sleep_log(logger, logging.ERROR))
def get_file_status(base_dir: str, job_hash: str) -> JobStatus:
    job_folder = os.path.join(base_dir, job_hash)
    if not os.path.exists(job_folder):
        return JobStatus.NOT_INITIALIZED

    slurm_files = glob.glob(os.path.join(job_folder, "slurm-*.out"))
    # slurm_status = self._read_slurm_status()
    if len(slurm_files) == 0:
        return JobStatus.NOT_SCHEDULED
    elif len(slurm_files) != 1:
        raise FileExistsError(
            "Found {} slurm files for job {}, expected one only.".format(
                len(slurm_files), job_hash))
    else:
        slurm_file = slurm_files[0]

    modified_time = os.path.getmtime(slurm_file)
    if time.time() - modified_time < 30:
        return JobStatus.RUNNING

    job_contents = subprocess.check_output(['tail', slurm_file],
                                           timeout=5).decode("utf8",
                                                             errors='ignore')
    if job_contents.find("DUE TO JOB REQUEUE") > -1:
        return JobStatus.PENDING
    if job_contents.find("Signaling Trainer to stop.") > -1:
        return JobStatus.COMPLETED
    return JobStatus.UNKNOWN
