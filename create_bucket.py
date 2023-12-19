import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    
   Bucket='mbrimage-boto3-12122023'
)

print(response)
