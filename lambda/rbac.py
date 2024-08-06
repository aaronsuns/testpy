import json
import boto3

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table('Users')
roles_table = dynamodb.Table('Roles')

def lambda_handler(event, context):
    user_id = event['requestContext']['authorizer']['claims']['sub']
    required_permission = event['queryStringParameters']['permission']

    # Fetch user data
    user_response = users_table.get_item(Key={'UserID': user_id})
    user_role = user_response.get('Item', {}).get('Role', None)

    if user_role:
        # Fetch role permissions
        role_response = roles_table.get_item(Key={'RoleName': user_role})
        role_permissions = role_response.get('Item', {}).get('Permissions', [])

        if required_permission in role_permissions:
            return {
                'statusCode': 200,
                'body': json.dumps('Access granted'),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }

    return {
        'statusCode': 403,
        'body': json.dumps('Access denied'),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
