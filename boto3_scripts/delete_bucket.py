import boto3

# Use the AWS credentials configured on this instance.
s3 = boto3.client("s3")

bucket_name = "tech613-thant-test-boto3"

# Delete the bucket once it is empty.
s3.delete_bucket(Bucket=bucket_name)
print(f"Deleted {bucket_name}")
