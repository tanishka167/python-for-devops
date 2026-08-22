import boto3

s3=boto3.client('s3')

# for bucket in s3.buckets.all():
#     if"ai-powered" in  bucket.name:
#         print(bucket.name)

file_name=r"C:\Users\tanishka\OneDrive\Documents\work\python-for-devops\day1\api.py"
object_name="api.py"
bucket="devops-ai-poweredt"



def upload_to_s3(file_name,bucket,object_name):
    response= s3.upload_file(file_name,bucket,object_name)

    return response.json