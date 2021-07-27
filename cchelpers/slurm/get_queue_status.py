import subprocess
import pandas as pd
from cchelpers.jobs import JobStatus
from io import BytesIO


def get_slurm_queue_df() -> pd.DataFrame:
    slurm_jobs = subprocess.check_output(['squeue', '-u', 'bgk'])
    jobs_df = pd.read_csv(BytesIO(slurm_jobs), delim_whitespace=True)
    jobs_df = jobs_df.rename(columns={"(REASON)": "REASON"})
    return jobs_df


def get_queue_status(slurm_id: int, jobs_df: pd.DataFrame) -> JobStatus:
    slurm_queue_status = jobs_df[jobs_df["JOBID"] == slurm_id]
    if len(slurm_queue_status) == 0:
        return JobStatus.NOT_SCHEDULED
    if len(slurm_queue_status) > 1:
        return JobStatus.ERROR

    slurm_queue_status = slurm_queue_status.iloc[0]
    # https://www.unix.com/man-page/debian/1/squeue/ - Job STATE CODES
    if slurm_queue_status["ST"] == "PD":
        return JobStatus.PENDING
    if slurm_queue_status["ST"] == "CG":
        return JobStatus.COMPLETING
    if slurm_queue_status["ST"] == "R":
        return JobStatus.RUNNING
    return JobStatus.UNKNOWN
