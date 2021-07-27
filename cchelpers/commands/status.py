import os
from p_tqdm import t_imap as mapper
import logging
import pprint
from cchelpers.slurm import get_job, get_slurm_queue_df
from cchelpers.jobs import JobList, JobStatus

logger = logging.getLogger(__name__)


def status(indir: str = "."):
    indir = os.path.abspath(indir)
    folders = [d for d in os.listdir(indir) if os.path.isdir(d)]

    jobs = JobList()

    print("Building slurm queue status")
    queue_df = get_slurm_queue_df()
    print("Done building slurm queue status, found {} entries".format(
        len(queue_df)))

    for job in mapper(lambda job_hash: get_job(job_hash, queue_df), folders):
        jobs.addJob(job)

    rerun = [j for j in jobs.jobs.values() if j.status == JobStatus.ERROR]
    pprint.pprint([r.job_hash for r in rerun])
