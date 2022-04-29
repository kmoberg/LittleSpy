![LittleSpy Banner](/Users/kmoberg/Projects/02-Origo/skjema-statuschecker/.github/github_banner.png)

# LittleSpy.io
Simple script that checks a specific address against the Bring API to check if it is up or not.
Pushes the response to Cloudwatch.

## Requirements
- MyBring API Key
- The instance or container that runs the script must have a CloudWatch role that allows for pushing to CloudWatch. (Example permission JSON is attached)

## Environment Variables
The following environment variables are required to be set:
- `MYBRINGAPIUID` This should be your email address from MyBring
- `MYBRINGAPIKEY` Your API key that you can get from your profile in MyBring


### Slack Notifications
If you want notifications sent to Slack when a status dips below a certain treshold, create an SNS topic that CloudWatch will send an alarm to, then deploy the [slack_lambda.py](slack_lambda.py) to send the alert to Slack. You'll need a Slack Webhook URL for this to work. 


**NOTE: Additionally, for local development and testing, you need to ensure you have AWS credentials loaded in your IDE or in your PATH!**