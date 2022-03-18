# Skjema - Bring API Status Checker
Simple script that checks a specific address against the Bring API to check if it is up or not.
Pushes the response to Cloudwatch.

## Requirements
- MyBring API Key
- The instance or container that runs the script must have a CloudWatch role that allows for pushing to CloudWatch. (Example permission JSON is attached)