import boto3




bucket = 'mbrimage-boto3-12122023'

key = 'test_text_string.txt'

filename = 'test_text_string.txt'

s3 = boto3.client('s3')

def download_single_object(client, bucket, key, filename ):
    client.download_file( bucket, key , filename)
    