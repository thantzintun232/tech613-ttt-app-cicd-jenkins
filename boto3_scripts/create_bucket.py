import boto3

# Use the AWS credentials configured on this instance.
s3 = boto3.client("s3", region_name="eu-west-1")

bucket_name = "tech613-thant-test-boto3"

# Create the bucket in Ireland.
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
)
print(f"Created {bucket_name}")
