from dataclasses import dataclass, field
from itertools import count


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
    id: int = field(default_factory=count().__next__)

    def insert_data(self):
        """

        :type table: object
        """
        from main import get_database

        status_code = self.status_code
        request_size = self.request_size
        request_headers = self.request_headers
        request_body = self.request_body
        response_size = self.response_size
        response_time = self.response_time
        headers = self.headers
        timestamp = self.timestamp
        domain = self.request_headers["url"]

        dbname = get_database()

        collection_name = dbname[domain]

        mydict = {
            "status_code": status_code,
            "request_size": request_size,
            "request_headers": request_headers,
            "request_body": request_body,
            "response_size": response_size,
            "response_time": response_time,
            "headers": headers,
            "timestamp": timestamp,
            "url": domain,
        }

        x = collection_name.insert_one(mydict)
        print(x.inserted_id)
        return x.inserted_id
