import json
import boto3
from botocore.exceptions import ClientError


def lookup_data(key, db=None, table='user-info'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    try:
        response = table.get_item(Key=key)
    except ClientError as e:
        print('Error', e.response['Error']['Message'])
    else:
        print(response['Item'])
        return response['Item']


def lambda_handler(event, context):
    q = event['queryStringParameters']
    username = q['username']
    password = q['password']

    # connect to DynamoDB
    db_result = lookup_data({'user_name': username})
    if password == db_result:
        return {
            'statusCode': 200,
            'body': json.dumps('Login Successfully.')
        }
    return {
        'statusCode': 404,
        'body': json.dump('Login Failed.')
    }