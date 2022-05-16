import boto3

rek_aws = boto3.client('rekognition',
            aws_access_key_id           = AWS_ACCESS_KEY,
            aws_secret_access_key       = AWS_SECRET_KEY,
            region_name                 = AWS_REGION)

with open('file.png', 'rb') as img_info:
     img = img_info.read()

rek_analysis =  rek_aws.detect_faces(Image={'Bytes':img}, Attributes=['ALL'])