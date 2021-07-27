from dataclasses import dataclass
from .JobStatus import JobStatus


@dataclass
class Job:
    job_hash: str
    slurm_id: int = None
    status: JobStatus = JobStatus.UNKNOWN
