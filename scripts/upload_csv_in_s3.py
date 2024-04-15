# File to upload
file_path = "charities_data.csv"

# Destination key
destination_key = "charities_data.csv"  # Update with the desired filename in the bucket

try:
    # Upload the file to the S3 bucket
    response = s3.upload_file(file_path, bucket_name, destination_key)
    print(
        f"File '{file_path}' uploaded successfully to '{bucket_name}' as '{destination_key}'."
    )
except Exception as e:
    print(f"Failed to upload file: {e}")
