from typing import Dict, Optional
from .Job import Job


class JobList:
    jobs: Dict[str, Job] = {}

    def addJob(self, job: Job) -> Job:
        self.jobs[job.job_hash] = job
        return self.getJob(job.job_hash)

    def getJob(self, job_hash: str) -> Optional[Job]:
        if job_hash not in self.jobs:
            return None
        return self.jobs[job_hash]

    def __len__(self):
        return len(self.jobs)
