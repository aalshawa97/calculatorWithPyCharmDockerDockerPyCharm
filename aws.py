import boto3

def create_s3_bucket(bucket_name):
    """
    Create an S3 bucket with the specified name.
    """
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"Creating bucket '{bucket_name}'.")

def upload_file_to_s3(file_path, bucket_name, object_key):
    """
    Upload a file to the specified S3 bucket.
    """
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_key)
    print(f"Uploaded file '{file_path}' to bucket '{bucket_name}' with object key '{object_key}'.")

# Specify the bucket name
bucket_name = 'exam-prep-bucket-2023'

# Create the S3 bucket
#create_s3_bucket(bucket_name)

# Upload a file to the S3 bucket
file_path = r"C:\Users\15039\Desktop\Images\python.jpg"
object_key = 'python.jpg'

# Upload the file
#upload_file_to_s3(file_path, bucket_name, object_key)

print(f"Uploading file '{file_path}' to bucket '{bucket_name}' with object key '{object_key}'.")
# Print a success message
#print(f" Creating bucket '{bucket_name}'.")