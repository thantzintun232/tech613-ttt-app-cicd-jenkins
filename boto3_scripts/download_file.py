import boto3

# Use the AWS credentials configured on this instance.
s3 = boto3.client("s3")

bucket_name = "tech613-thant-test-boto3"

# Save the S3 file under a new name on EC2.
s3.download_file(bucket_name, "test.txt", "downloaded_test.txt")
print("Downloaded test.txt to downloaded_test.txt")
