from enum import Enum


class CheckStatus(str, Enum):
    PASS = "PASS"
    WARNING = "WARNING"
    FAIL = "FAIL"


class Priority(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"