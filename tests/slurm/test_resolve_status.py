from cchelpers.slurm.resolve_status import resolve_status
from cchelpers.jobs import JobStatus


class TestResolveStatus():

    def test_all_combinations_considered(self):
        for file_status in JobStatus:
            for queue_status in JobStatus:
                status = resolve_status(queue_status, file_status)
                assert status == JobStatus.ERROR or status == file_status or status == queue_status
