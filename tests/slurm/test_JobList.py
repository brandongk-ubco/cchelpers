from cchelpers.jobs import JobList, Job
from uuid import uuid4


class TestJobList():

    def test_job_list(self):
        job_hashes = []
        jobs = []
        jl = JobList()
        assert len(jl) == 0
        for i in range(100):
            job_hash = uuid4()
            job = Job(job_hash=job_hash)
            job_hashes.append(job_hash)
            jobs.append(job)
            jl.addJob(job)
            assert len(jl) == i
        assert len(jl) == 100
        for i, job_hash in enumerate(job_hashes):
            assert jl.getJob(job_hash) == jobs[i]

    def test_no_job(self):
        job_hash = uuid4()
        jl = JobList()
        assert jl.getJob(job_hash) is None
