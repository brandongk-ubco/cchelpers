from enum import Enum


class JobStatus(Enum):
    UNKNOWN = 0
    NOT_INITIALIZED = 1
    NOT_SCHEDULED = 2
    PENDING = 3
    RUNNING = 4
    COMPLETED = 5
    ERROR = 6
