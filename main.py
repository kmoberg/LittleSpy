import datetime
import json
import logging
import os

import requests

from models.checks import RequestObject


def check_url(url, request_headers, request_body):
    try:
        r = requests.get(url, headers=request_headers, data=request_body)
        return RequestObject(
            status_code=r.status_code,
            request_size=r.__sizeof__(),
            request_headers=request_headers,
            request_body=request_body,
            response_size=r.__sizeof__(),
            response_time=r.elapsed.total_seconds(),
            headers=dict(r.headers),
            timestamp=datetime.datetime.now().timestamp(),
        )
    except requests.ConnectTimeout:
        return "Connection Timeout"
    except requests.ConnectionError:
        return "Connection Error"


def get_database():
    from pymongo import MongoClient

    mongo_user = os.environ.get("MONGODB_USER")
    mongo_password = os.environ.get("MONGODB_PASSWORD")
    mongo_host = os.environ.get("MONGODB_URI")
    mongo_port = os.environ.get("MONGODB_PORT")
    mongo_db = os.environ.get("MONGODB_DATABASE")

    CONNECTION_STRING = (
        f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}"
    )

    client = MongoClient(CONNECTION_STRING)

    return client[mongo_db]


def main():

    url = "https://nyartcc.org"
    request_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/81.0.4044.138 Safari/537.36",
        "url": url,
    }
    request_body = {"key": "value"}

    check = check_url(url, request_headers, request_body)

    logging.debug(f"Status Code: {check.status_code}")
    logging.debug(f"Request Size: {check.request_size}")
    logging.debug(f"Request Headers: {check.request_headers}")
    logging.debug(f"Request Body: {check.request_body}")
    logging.debug(f"Response Size: {check.response_size}")
    logging.debug(f"Response Time: {check.response_time}")
    logging.debug(json.dumps(check.response_headers, indent=4))
    logging.debug(f"Timestamp: {datetime.datetime.fromtimestamp(check.timestamp)}")
    logging.debug(f'Domain: {check.request_headers["url"]}')

    check.insert_data()


if __name__ == "__main__":
    level = logging.DEBUG
    fmt = "[%(levelname)s] %(asctime)s - %(message)s"
    logging.basicConfig(level=level, format=fmt)

    main()
