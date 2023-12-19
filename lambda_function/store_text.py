import json
import boto3


# Initialize AWS clients
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    bucket = str(event["Records"][0]['s3']['bucket']['name'])
    key = str(event["Records"][0]['s3']['object']['key'])

    data = s3_client.get_object(Bucket=bucket, Key=key)
    json_data = data['Body'].read().decode('utf-8')
    json_data = json.loads(json_data)
    text = json_data["results"]["transcripts"][0]["transcript"]

    file_name = key[:key.find(".")]
    destination_bucket = 'input-text-store'
    destination_key = f"{file_name}.txt"

    # input in text format
    s3_client.put_object(Bucket=destination_bucket, Key=destination_key, Body=text)
