from typing import Dict
from .Job import Job


class JobList:
    jobs: Dict[str, Job] = {}

    def addJob(self, job: Job) -> Job:
        self.jobs[job.job_hash] = job
        return self.getJob(job.job_hash)

    def getJob(self, job_hash: str) -> Job:
        return self.jobs[job_hash]

    def updateJob(self, job: Job) -> Job:
        self.jobs[job.job_hash].update(Job)
        return self.getJob(job.job_hash)
