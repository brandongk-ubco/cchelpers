from enum import Enum


class JobStatus(Enum):
    UNKNOWN = 0
    NOT_SCHEDULED = 1
    PENDING = 2
    RUNNING = 3
    COMPLETING = 4
    COMPLETED = 5
    ERROR = 6
    NOT_INITIALIZED = 7
