import boto3

s3 = boto3.client('s3')

#The code below uploads an new object to an existing bucket in AWS s3

s3.put_object(Bucket ='mbrimage-boto3-12122023', Key = 'test_text_string.txt', Body ="Hey this is a string"
, ContentType = 'text/plain')
