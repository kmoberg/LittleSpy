#!/usr/bin/python3.6
import urllib3
import json

http = urllib3.PoolManager()


def lambda_handler(event, context):
    url = "#################"
    msg = {
        "channel": "#CHANNEL_NAME",
        "text": event['Records'][0]['Sns']['Message'],
        "accessory": {
            "type": "image",
            "image_url": "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",
            "alt_text": "calendar thumbnail"
        }
    }

    encoded_msg = json.dumps(msg, indent=4).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'],
        "status_code": resp.status,
        "response": resp.data
    })