import boto3
import logging
logging.basicConfig(filename='logs\general_log.log', level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s ====: %(message)s =;',
    datefmt='%Y-%m-%d %H:%M:%S')

ACCESS_KEY = 'ASIAVLMAXETSNQQY6PHA'
SECRET_KEY ='UPJC1Nsbz56yoMSfAUEWIzi5doNb+gMDxLcN+Okl'
SESSION_TOKEN='FwoGZXIvYXdzEHgaDDVok6s6cd3yZntE8CLTAQKeSmuecAVLzKnJUaFUBqQu45CqTTB3ZdmkA/ptPLiDz2j9Rv7xkchDUCZWCHWy3iDTf/6+hOX/2d3RS4XxRWsKffR9+EzhTzhMtTbm6WWv0uRUYklyqbCfTnkVpjx/XdY1L2uICo4HudwdZ1vTHhquKAUQw+QGuzaoLXLOPEXx6LRnHuJqlGka79Zab2q/wyLTJzYGzbpOlm9vU3/JArg02bXZq+vbs8+cSFtdUp4R0I14Y0ecrG7UO+Ltylme+Ck5gPGQcoFsM/K6jBPcpYEUZWgo3vyqlAYyLYkjNRDCuxGNBFE/AXG1o3xQVu6BkwxiUlY5T9jmz3PBmnmv6R/lFvH25pHToQ=='

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
               
          
          ,SimilarityThreshold = 0,
          )
          simil = rek_response['FaceMatches'][0]['Similarity']
          logging.info("Comparação realizada com sucesso!")
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

     try:
          a, file_name = file_path.split("/")
          bucket_name = 'psi4-lf'
          aws_file_path = '{}/{}'.format(file_goto, file_name)
          
          s3 = boto3.client('s3',
          aws_access_key_id = ACCESS_KEY,
          aws_secret_access_key = SECRET_KEY,
          aws_session_token= SESSION_TOKEN)

          s3.upload_file(file_path, bucket_name, aws_file_path)
          logging.info("Imagem enviada para o S3 com sucesso")
     except:
          logging.info("Erro no envio para o S3.")
     
#sendImgS3('img/2022-5-22_20-7-38.png','test')
#getReckres("img\edf.jpeg")