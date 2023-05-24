#Abdullah Mutaz Alshawa
#5/24/23
import urllib.request
import boto3

# Perform a simple GET request to the AWS homepage
response = urllib.request.urlopen('https://aws.amazon.com')

# Read and print the response
data = response.read()
print(data)

import boto3

# Set your AWS access key ID and secret access key
access_key_id = 'YOUR_KEY'
secret_access_key = 'YOUR_SECURITY_KEY'

# Create an S3 client with your credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key
)

# Now you can use the S3 client to interact with Amazon S3
# For example, you can list your S3 buckets
response = s3_client.list_buckets()
buckets = response['Buckets']

# Print the names of all your S3 buckets
for bucket in buckets:
    print(bucket['Name'])
