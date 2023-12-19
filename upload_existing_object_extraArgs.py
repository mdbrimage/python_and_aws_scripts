import boto3


#The code below uploads an existing file to an existing AWS s3 bucket

s3 = boto3.client('s3')

s3.upload_file('/home/ec2-user/environment/python_scripts/test_text.txt'
, 'mbrimage-boto3-12122023', 'test_text_upload.txt',ExtraArgs = {'ContentType': 'text/plain' })
