from enum import Enum
class Responsesignal(Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
    ERROR = "Error"
    NOT_FOUND = "Not Found"
    UNAUTHORIZED = "Unauthorized"
    FORBIDDEN = "Forbidden"
    BAD_REQUEST = "Bad Request"