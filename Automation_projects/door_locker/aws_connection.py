import boto3

ACCESS_KEY = ' '
SECRET_KEY ='QjnAVFMlJn+ + '
SESSION_TOKEN=' +2NT3Nc65Yt+ +x6EDW+ / + + / + / /+aA=='

def getReckres(imgname):
     rek_aws = boto3.client('rekognition',
     aws_access_key_id = ACCESS_KEY,
     aws_secret_access_key = SECRET_KEY,
     aws_session_token= SESSION_TOKEN)
     try:
          imageTarget = open(imgname,'rb')
          rek_response = rek_aws.compare_faces(
          SourceImage={
                    "S3Object": {
                         "Bucket": 'psi4-lf',
                         "Name": "Registered/Resident1.png",
                    }
               },
               TargetImage= {'Bytes': imageTarget.read()}
               
          
          ,SimilarityThreshold=80,
          )
          simil = rek_response['FaceMatches'][0]['Similarity']
          if float(simil) > 90:
               print(simil)
               return(True, True)
          else:
               print(simil)
               return(False, True)
     except:
          print("n")
          return(False, False)


def sendImgS3(file_path, file_name, file_goto):
     #file_path = 'img/test.png'
     bucket_name = 'psi4-lf'
     aws_file_path = '{}/{}.png'.format(file_goto, file_name)
     
     s3 = boto3.client('s3',
     aws_access_key_id = ACCESS_KEY,
     aws_secret_access_key = SECRET_KEY,
     aws_session_token= SESSION_TOKEN)

     s3.upload_file(file_path, bucket_name, aws_file_path)
     
#sendImgS3()
getReckres("img\edf.jpeg")
