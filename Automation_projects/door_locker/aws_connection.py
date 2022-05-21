import boto3

ACCESS_KEY = ''
SECRET_KEY ='/L0GZB7Ujpm'
SESSION_TOKEN='++///+++/+=='

def getReckres(imgname):
     rek_aws = boto3.client('rekognition',
     aws_access_key_id = ACCESS_KEY,
     aws_secret_access_key = SECRET_KEY,
     aws_session_token= SESSION_TOKEN)
     rek_response = rek_aws.compare_faces(
	    SourceImage={
			"S3Object": {
				"Bucket": 'psi4-lf',
				"Name": key,
			}
		},
		TargetImage={
			"S3Object": {
				"Bucket": 'psi4-lf',
				"Name": key_target,
			}
		},
	    SimilarityThreshold=80,
	)
     simil = rek_response['FaceMatches']['Similarity']
     if float(simil[:-1]) > 93:
          return(True)
     else:
          return(False)


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