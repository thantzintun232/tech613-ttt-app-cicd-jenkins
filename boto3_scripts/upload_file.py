import boto3

# Use the AWS credentials configured on this instance.
s3 = boto3.client("s3")

bucket_name = "tech613-thant-test-boto3"

# Upload the local file as test.txt in S3.
s3.upload_file("test.txt", bucket_name, "test.txt")
print("Uploaded test.txt")
