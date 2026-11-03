import boto3

# Use the AWS credentials configured on this instance.
s3 = boto3.client("s3")

bucket_name = "tech613-thant-test-boto3"

# Delete test.txt from S3.
s3.delete_object(Bucket=bucket_name, Key="test.txt")
print("Deleted test.txt")
