from dataclasses import dataclass


@dataclass
class RequestObject:
    status_code: int
    request_size: int
    request_headers: dict
    request_body: dict
    response_size: int
    response_time: float
    headers: dict
    timestamp: float
