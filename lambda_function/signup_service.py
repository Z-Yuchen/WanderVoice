import json
import boto3
from botocore.exceptions import ClientError


def check_username(key, db=None, table='user-info'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    try:
        response = table.get_item(Key=key)
        print(response['Item'])
        return False
    except ClientError as e:
        return True


def insert_data(usr, passwd, db=None, table='user-info'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    # upload username and password
    data = {"user_name": usr, "pass_word": passwd}
    try:
        response = table.put_item(Item=data)
        return True
    except ClientError as e:
        return False


def lambda_handler(event, context):
    q = event['queryStringParameters']
    username = q['username']
    password = q['password']

    # Check whether the username has existed
    if check_username(username):
        result = insert_data(username, password)
        if result:
            return {
                'statusCode': 200,
                'body': json.dumps('Register Successfully')
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Register Fail.')
            }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('The username has been used.')
        }