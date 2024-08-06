import json
import boto3
from jose import jwt

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    try:
        # Validate the JWT token using Cognito public keys
        # Assuming Cognito User Pool is used for authentication
        user_info = jwt.decode(token, verify=True)

        return {
            'statusCode': 200,
            'body': json.dumps('User authenticated'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except jwt.JWTError as e:
        return {
            'statusCode': 401,
            'body': json.dumps('Unauthorized'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
