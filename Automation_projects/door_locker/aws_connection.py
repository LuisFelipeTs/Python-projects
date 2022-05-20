import boto3

def getReckres():
     rek_aws = boto3.client('rekognition')

     with open('file.png', 'rb') as img_info:     
          img = img_info.read()

     rek_analysis =  rek_aws.detect_faces(Image={'Bytes':img}, Attributes=['ALL'])

def sendImgS3(img_path):
     bucket_name = "psi4-lf"
     
     pass
