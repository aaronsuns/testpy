import json
import boto3
from jose import jwt

def lambda_handler(event, context):
    # Retrieve the JWT token from the Authorization header
    token = event['headers'].get('Authorization')

    # Ensure the token is in the expected format
    if token is None or not token.startswith('Bearer '):
        return {
            'statusCode': 401,
            'body': json.dumps('Unauthorized'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    token = token.split(' ')[1]  # Extract the token part

    try:
        # Validate the JWT token using Cognito public keys
        # (Assuming you have the correct public keys and configurations)
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
