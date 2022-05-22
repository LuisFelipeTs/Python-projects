import boto3
import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S')

ACCESS_KEY = ''
SECRET_KEY = ''
SESSION_TOKEN = ''
def getReckres(img_path):
     rek_aws = boto3.client('rekognition',
     aws_access_key_id = ACCESS_KEY,
     aws_secret_access_key = SECRET_KEY,
     aws_session_token= SESSION_TOKEN)
     try:
          altual_registered_target = "Registered/Resident1.png"
          imageTarget = open(img_path,'rb')
          rek_response = rek_aws.compare_faces(
          SourceImage={
                    "S3Object": {
                         "Bucket": 'psi4-lf',
                         "Name": altual_registered_target,
                    }
               },
               TargetImage= {'Bytes': imageTarget.read()}
               
          
          ,SimilarityThreshold=80,
          )
          simil = rek_response['FaceMatches'][0]['Similarity']
          logging.info("Comparação realizada com secesso!")
          if float(simil) > 94:
               print(simil)
               return(True, True)
          else:
               print(simil)
               return(False, True)
     except:
          logging.info("Falha na comparação das imagens")
          return(False, False)


def sendImgS3(file_path, file_goto):
     a, file_name = file_path.split('/')
     bucket_name = 'psi4-lf'
     aws_file_path = '{}/{}.png'.format(file_goto, file_name)
     
     s3 = boto3.client('s3',
     aws_access_key_id = ACCESS_KEY,
     aws_secret_access_key = SECRET_KEY,
     aws_session_token= SESSION_TOKEN)

     s3.upload_file(file_path, bucket_name, aws_file_path)
     logging.info("Imagem enviada para o bucket com secesso")
     
#sendImgS3()
#getReckres("img\edf.jpeg")
