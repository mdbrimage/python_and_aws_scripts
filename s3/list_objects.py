import boto3

s3 = boto3.client('s3')

#listing the objects in mbrimage-boto3-12122023 bucket
response = s3.list_objects_v2(Bucket= 'mbrimage-boto3-12122023') 

for content in response['Contents']:
    if ('.txt' in content['Key'][-4:] ): #searches only for file extenstions with .txt in the last 4 chars
        print(content['Key'])
    
