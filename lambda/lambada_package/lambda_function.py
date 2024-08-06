import json
import boto3
import jwt  # Ensure this is pyjwt, not jose

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    try:
        user_info = jwt.decode(token, options={"verify_signature": False})

        return {
            'statusCode': 200,
            'body': json.dumps('User authenticated'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except jwt.ExpiredSignatureError:
        return {
            'statusCode': 401,
            'body': json.dumps('Token has expired'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except jwt.InvalidTokenError:
        return {
            'statusCode': 401,
            'body': json.dumps('Invalid token'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
