"""
Your module description
"""

import boto3

def filter_objects_extentions(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket = bucket)
    for content in response['Contents']:
        if (extension in content['Key'][-(len(extension)):]): #searches only for designated file extenstions with 
           keys.append(content['Key'])
    return keys
    
'''
s3 = boto3.client('s3')

response = filter_objects_extentions(s3, 'mbrimage-boto3-12122023', '.txt')

print(response)

'''
