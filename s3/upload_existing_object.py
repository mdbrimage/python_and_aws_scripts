import boto3

s3 = boto3.client('s3')
#The code below uploads an existing object to an existing bucket in AWS s3

with open('/home/ec2-user/environment/python_scripts/test_text.txt', 'rb') as f: 
    s3.put_object(Bucket ='mbrimage-boto3-12122023', Key = 'test_text.txt', Body = f, ContentType = 'text/plain')
