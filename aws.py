import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Specify the bucket name
bucket_name = 'exam-prep-bucket-2023'


# Create the S3 bucket
#s3_client.create_bucket(Bucket=bucket_name)

# Print a success message
print(f" Creating bucket '{bucket_name}'.")
# Upload a file to the S3 bucket
#file_path = r"C:\Users\15039\Desktop\Images\python.jpg"
#object_key = 'python.jpg'

# Upload the file
#s3_client.upload_file(file_path, bucket_name, object_key)
