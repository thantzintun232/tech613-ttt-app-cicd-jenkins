# AWS S3 on Ubuntu EC2

## Part 1 - Manage S3 with the AWS CLI

## 1. What is S3?

- **S3** (Simple Storage Service) stores files in the cloud.
- Files are kept in **buckets**. Each file is an **object**.
- Very durable: AWS keeps copies in at least 3 availability zones in a region.
- Files are **private** unless you make them public.
- Use it with the **AWS CLI** (commands) or the **AWS console** (website).

---

## 2. Set up

**Install the AWS CLI** on a fresh Ubuntu EC2 instance.
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install unzip -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

**Log in:**

```
aws configure
```

| Question | Enter |
|---|---|
| Access Key ID | From your CSV file |
| Secret Access Key | From your CSV file |
| Default region | `eu-west-1` |
| Output format | `json` |

**Check it works:**

```
aws configure list   # keys and region should be set
aws s3 ls            # lists buckets
```

---

## 3. Commands

Replace `tech613-thant-first-bucket` with your own bucket name.

| Task | Command |
|---|---|
| List all buckets | `aws s3 ls` |
| Make a bucket | `aws s3 mb s3://tech613-thant-first-bucket` |
| Create a test file | `echo "first line" > test.txt` |
| Upload a file | `aws s3 cp test.txt s3://tech613-thant-first-bucket` |
| List files in a bucket | `aws s3 ls s3://tech613-thant-first-bucket` |
| Download everything | `aws s3 sync s3://tech613-thant-first-bucket .` |
| Delete one file | `aws s3 rm s3://tech613-thant-first-bucket/test.txt` |
| Get help | `aws s3 help` or `aws s3 rm help` |

Notes:

- Download into a separate folder (`mkdir downloads && cd downloads`) so `sync` does not overwrite your files.
- The `.` at the end of `sync` means "this folder".
- `rm` deletes from the cloud only. Your local copy stays.
- Always check with `aws s3 ls s3://bucket-name` after a change.

---

## 4. Dangerous commands

| Command | What it does |
|---|---|
| ⚠️ `aws s3 rm s3://bucket-name --recursive` | Deletes **all files** in the bucket |
| ☠️ `aws s3 rb s3://bucket-name --force` | Deletes the **bucket and all its files** |

`aws s3 rb s3://bucket-name` (no `--force`) only removes an **empty** bucket.

## Part 2 — Manage S3 with Python and Boto3

Use the same EC2 instance and AWS credentials from Part 1. The Python scripts use a separate bucket named `tech613-thant-test-boto3`.

### Set up Python

From the folder containing the scripts, run:

```
sudo apt install -y python3-venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install boto3
echo "Hello from my EC2 instance" > test.txt
```

### Run the scripts in order

| Command | What it does |
|---|---|
| `python3 list_buckets.py` | Lists the buckets in your AWS account. [Script](../boto3_scripts/list_buckets.py)  |
| `python3 create_bucket.py` | Creates the test bucket in Ireland (`eu-west-1`). [Script](../boto3_scripts/create_bucket.py) |
| `python3 upload_file.py` | Uploads `test.txt` to the bucket. [Script](../boto3_scripts/upload_file.py) |
| `python3 download_file.py` | Downloads the object as `downloaded_test.txt`. [Script](../boto3_scripts/download_file.py) |
| `python3 delete_file.py` | Removes `test.txt` from S3. [Script](../boto3_scripts/delete_file.py) |
| `python3 delete_bucket.py` | Removes the empty bucket. [Script](../boto3_scripts/delete_bucket.py) |

### Check the results

- After uploading, run `aws s3 ls s3://tech613-thant-test-boto3/` and check for `test.txt`.
- After downloading, run `cat downloaded_test.txt` and check for `Hello from my EC2 instance`.
- After deleting the file, list the bucket contents again. The bucket should be empty.
- After deleting the bucket, run `aws s3 ls` and check that the bucket is gone.
