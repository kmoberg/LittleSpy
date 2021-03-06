#!/home/ec2-user/venv/bin/python3

import os
import sys
import time
import requests
import boto3


def put_cloudwatch_logs(logs):
    AWS_REGION = "eu-north-1"
    client = boto3.client('cloudwatch', region_name=AWS_REGION)

    if logs[1] == 200:
        status_code = 1
        print("Status Code:", logs[1])
    elif logs[1] == 401:
        status_code = 0.5
        print("Error 401, unauthorized")
    else:
        status_code = 0
        print("Status Code:", logs[1])

    response = client.put_metric_data(
        Namespace='Bring API Status',
        MetricData=[
            {
                'MetricName': 'Status',
                'Dimensions': [
                    {
                        'Name': 'Status Code',
                        'Value': str(logs[1])
                    }
                ],
                'Value': status_code,
                'Unit': 'Count'
            },
            {
                'MetricName': 'Response Time',
                'Dimensions': [
                    {
                        'Name': 'Response Time',
                        'Value': 'Seconds'
                    }
                ],
                'Value': logs[2],
                'Unit': 'Seconds'
            }
        ]
    )
    print(response)


def get_status(url):
    """
    Get the statuscode and response from the specified URL.
    :param url:
    :return:
    """

    if not "MYBRINGAPIUID" and "MYBRINGAPIKEY" in os.environ:
        sys.exit("❌ Error! Ensure the environemnt variables 'MYBRINGAPIUID' and 'MYBRINGAPIKEY' are set!")

    headers = {
        "X-Mybring-API-Uid": os.getenv('MYBRINGAPIUID'),
        "X-Mybring-API-Key": os.getenv('MYBRINGAPIKEY')
    }
    params = {"address_type": "street", "street_or_place": "slottsplassen"}
    r = requests.get(url, headers=headers, params=params)

    response_content = r.content.decode("utf-8")

    print(r.status_code, r.elapsed.microseconds/10000000)
    current_time = time.time()

    # For local development and debugging, store a local CSV file.
    try:
        f = open('statistics.csv', 'a')

        # Timestamp, Status_Code, Response_Duration, Response
        text = "{},{},{},{}\n".format(current_time, r.status_code, r.elapsed.seconds, response_content)
        try:
            f.write(text)
        finally:
            f.close()
    except IOError as e:
        print("Oops!", e)

    return current_time, r.status_code, r.elapsed.microseconds/10000000, response_content


if __name__ == '__main__':

    check_status = get_status("https://api-new.bring.com/address/api/no/addresses")
    print(list(check_status))

    put_cloudwatch_logs(check_status)

