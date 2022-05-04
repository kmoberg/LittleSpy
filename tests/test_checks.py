from models.checks import RequestObject


def test_RequestObject():
    obj1 = RequestObject(
        status_code=200,
        request_size=32,
        request_headers={"Content-Type": "application/json", "url": "http://test.com"},
        request_body={"test": "test"},
        response_size=32,
        response_time=0.1,
        response_headers={"Content-Type": "application/json", "url": "http://test.com"},
        timestamp=123456789.0,
    )

    assert type(obj1.status_code) is int
    assert type(obj1.request_size) is int
    assert type(obj1.request_headers) is dict
    assert type(obj1.request_body) is dict
    assert type(obj1.response_size) is int
    assert type(obj1.response_time) is float
    assert type(obj1.response_headers) is dict
    assert type(obj1.timestamp) is float
    assert type(obj1.id) is int
