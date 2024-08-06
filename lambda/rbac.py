import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user_id = event['requestContext']['authorizer']['claims']['sub']
    required_permission = event['queryStringParameters']['permission']

    response = table.get_item(Key={'UserID': user_id})
    user_permissions = response.get('Item', {}).get('Permissions', [])

    if required_permission in user_permissions:
        return {
            'statusCode': 200,
            'body': json.dumps('Access granted'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    else:
        return {
            'statusCode': 403,
            'body': json.dumps('Access denied'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
