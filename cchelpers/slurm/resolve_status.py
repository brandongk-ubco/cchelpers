from cchelpers.jobs import JobStatus


def resolve_status(queue_status, file_status):

    if file_status == JobStatus.ERROR:
        return JobStatus.ERROR
    if queue_status == JobStatus.ERROR:
        return JobStatus.ERROR

    if file_status == JobStatus.UNKNOWN and queue_status == JobStatus.UNKNOWN:
        return JobStatus.ERROR

    if queue_status == JobStatus.COMPLETED:
        return JobStatus.ERROR
    if queue_status == JobStatus.NOT_INITIALIZED:
        return JobStatus.ERROR

    if file_status == queue_status:
        return file_status

    if file_status == JobStatus.UNKNOWN and queue_status == JobStatus.PENDING:
        return JobStatus.PENDING
    if file_status == JobStatus.UNKNOWN and queue_status == JobStatus.NOT_SCHEDULED:
        return JobStatus.ERROR
    if file_status == JobStatus.UNKNOWN and queue_status == JobStatus.RUNNING:
        return JobStatus.RUNNING

    if file_status == JobStatus.NOT_INITIALIZED and queue_status == JobStatus.PENDING:
        return JobStatus.NOT_INITIALIZED
    if file_status == JobStatus.NOT_INITIALIZED and queue_status == JobStatus.NOT_SCHEDULED:
        return JobStatus.NOT_INITIALIZED
    if file_status == JobStatus.NOT_INITIALIZED and queue_status == JobStatus.RUNNING:
        return JobStatus.NOT_INITIALIZED
    if file_status == JobStatus.NOT_INITIALIZED and queue_status == JobStatus.UNKNOWN:
        return JobStatus.NOT_INITIALIZED

    if file_status == JobStatus.NOT_SCHEDULED and queue_status == JobStatus.PENDING:
        return JobStatus.PENDING
    if file_status == JobStatus.NOT_SCHEDULED and queue_status == JobStatus.RUNNING:
        return JobStatus.RUNNING
    if file_status == JobStatus.NOT_SCHEDULED and queue_status == JobStatus.UNKNOWN:
        return JobStatus.ERROR

    if file_status == JobStatus.PENDING and queue_status == JobStatus.NOT_SCHEDULED:
        return JobStatus.ERROR
    if file_status == JobStatus.PENDING and queue_status == JobStatus.RUNNING:
        return JobStatus.ERROR
    if file_status == JobStatus.PENDING and queue_status == JobStatus.UNKNOWN:
        return JobStatus.RUNNING

    if file_status == JobStatus.RUNNING and queue_status == JobStatus.NOT_SCHEDULED:
        return JobStatus.ERROR
    if file_status == JobStatus.RUNNING and queue_status == JobStatus.PENDING:
        return JobStatus.ERROR
    if file_status == JobStatus.RUNNING and queue_status == JobStatus.UNKNOWN:
        return JobStatus.ERROR

    if file_status == JobStatus.COMPLETED and queue_status == JobStatus.PENDING:
        return JobStatus.ERROR
    if file_status == JobStatus.COMPLETED and queue_status == JobStatus.NOT_SCHEDULED:
        return JobStatus.COMPLETED
    if file_status == JobStatus.COMPLETED and queue_status == JobStatus.RUNNING:
        return JobStatus.COMPLETED
    if file_status == JobStatus.COMPLETED and queue_status == JobStatus.UNKNOWN:
        return JobStatus.COMPLETED

    raise ValueError(
        "Invalid combination of file status {} and queue_status {}".format(
            file_status, queue_status))
