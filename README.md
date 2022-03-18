# Skjema - Bring API Status Checker
Simple script that checks a specific address against the Bring API to check if it is up or not.
Pushes the response to Cloudwatch.

## Requirements
- MyBring API Key
- The instance or container that runs the script must have a CloudWatch role that allows for pushing to CloudWatch. (Example permission JSON is attached)

## Environment Variables
The following environment variables are required to be set:
- `Mybring-API-Uid` This should be your email address from MyBring
- `Mybring-API-Key` Your API key that you can get from your profile in MyBring

**NOTE: Additionally, for local development and testing, you need to ensure you have AWS credentials loaded!**