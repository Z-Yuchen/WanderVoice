import boto3


# Initialize AWS clients
transcribe_client = boto3.client('transcribe')
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    # Define the source S3 bucket and file names
    source_bucket = str(event["Records"][0]['s3']['bucket']['name'])
    source_file_key = str(event["Records"][0]['s3']['object']['key'])
    # Fetch the text content from the source S3 bucket
    object_url = 'https://s3.amazonaws.com/{0}/{1}'.format(source_bucket, source_file_key)
    transcribe_client.start_transcription_job(
        TranscriptionJobName=source_file_key[:source_file_key.find(".")],
        LanguageCode='es-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': object_url
        },
        OutputBucketName='transcribe-temp-folder'
    )
