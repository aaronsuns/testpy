import json
import boto3
from PIL import Image
import io

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the bucket name and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the image from S3
    response = s3.get_object(Bucket=source_bucket, Key=key)
    image_content = response['Body'].read()

    # Open the image with Pillow
    image = Image.open(io.BytesIO(image_content))

    # Resize the image
    image = image.resize((100, 100))

    # Save the resized image to a buffer
    buffer = io.BytesIO()
    image.save(buffer, 'JPEG')
    buffer.seek(0)

    # Upload the resized image to the destination bucket
    destination_bucket = 'destination-bucket'
    s3.put_object(Bucket=destination_bucket, Key=key, Body=buffer, ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed and uploaded successfully')
    }
