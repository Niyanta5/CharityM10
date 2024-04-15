import boto3

# Create an S3 client using the default credential provider chain
s3 = boto3.client("s3")

# Define bucket name
bucket_name = "charities-bucket"
region_name = "us-east-1"  # Specify the desired region

try:
    # Create the bucket without specifying the location constraint
    response = s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully in region '{region_name}'.")
except Exception as e:
    print(f"Failed to create bucket: {e}")
