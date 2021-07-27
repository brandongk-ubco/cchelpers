from .get_id import get_id
from .get_file_status import get_file_status
from .get_queue_status import get_queue_status
from .resolve_status import resolve_status
from cchelpers.jobs import Job
import pandas as pd


def get_job(base_dir: str, job_hash: str, queue_df: pd.DataFrame) -> Job:
    slurm_id = get_id(base_dir, job_hash)
    file_status = get_file_status(base_dir, job_hash)
    queue_status = get_queue_status(slurm_id, queue_df)
    try:
        job_status = resolve_status(queue_status, file_status)
    except ValueError as err:
        if not err.args:
            err.args = ('',)
        err.args = ("Error processing job {} with slurm ID {}: ".format(
            job_hash, slurm_id),) + err.args
        raise

    return Job(job_hash=job_hash, slurm_id=slurm_id, status=job_status)
