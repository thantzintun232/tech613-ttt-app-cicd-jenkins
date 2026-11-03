import boto3

# Use the AWS credentials configured on this instance.
s3 = boto3.client("s3")

# Print the name of each bucket.
for bucket in s3.list_buckets()["Buckets"]:
    print(bucket["Name"])
