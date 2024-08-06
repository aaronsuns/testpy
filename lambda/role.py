import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserRoles')

def lambda_handler(event, context):
    user_id = event['requestContext']['authorizer']['claims']['sub']
    required_role = event['queryStringParameters']['role']

    response = table.get_item(Key={'UserID': user_id})
    user_role = response.get('Item', {}).get('Role')

    if user_role == required_role:
        return {
            'statusCode': 200,
            'body': json.dumps('Access granted')
        }
    else:
        return {
            'statusCode': 403,
            'body': json.dumps('Access denied')
        }
