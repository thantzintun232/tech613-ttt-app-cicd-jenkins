# AWS Deployment, Monitoring and Auto Scaling

My notes from deploying a Node.js application on AWS during the Sparta Global Cloud DevOps programme. These guides cover automated deployment, reusable machine images, MongoDB, monitoring, load balancing and Auto Scaling.

## Guides

| Guide | What it covers |
|---|---|
| [App deployment with user data](documents/app-user-data-automation.md) | Automating application setup when an EC2 instance launches. |
| [Creating an AMI](documents/creating-ami-documentation.md) | Saving a configured instance as an image and launching new instances from it. |
| [MongoDB deployment](documents/mongodb_deployment.md) | Setting up MongoDB, connecting the app and enabling automatic startup. |
| [Monitoring and CPU alerts](documents/monitoring.md) | CloudWatch dashboards, ApacheBench load testing and email alerts for high CPU usage. |
| [Auto Scaling and load balancing](documents/autoscaling.md) | Launch templates, load balancing, CPU-based scaling and automatic instance replacement. |
| [VPC setup](documents/vpc_documentation.md) | Setting up a VPC for the application and database. |
| [Amazon S3](documents/s3_notes.md) | Managing buckets and files with the AWS CLI and Python Boto3. |

Start with app deployment, then follow the AMI, MongoDB, monitoring and Auto Scaling guides.

## Tools used

AWS EC2, AMIs, User Data, Auto Scaling Groups, Application Load Balancer, CloudWatch, SNS, Bash, Node.js, Nginx, PM2, MongoDB and ApacheBench.

## Repository layout

- `README.md` — repository homepage
- `documents/app-user-data-automation.md` — app automation guide
- `documents/creating-ami-documentation.md` — AMI guide
- `documents/mongodb_deployment.md` — database setup guide
- `documents/monitoring.md` — monitoring and alerts guide
- `documents/autoscaling.md` — Auto Scaling and load balancing guide
- `documents/vpc_documentation.md` — VPC setup guide
- `documents/s3_notes.md` — S3 CLI and Boto3 guide
- `images/` — screenshots used in the guides
