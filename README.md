# Upload Files to Amazon S3 through a Directory

This is a demo of setting up an Amazon Web Service (AWS) S3 bucket and uploading a file with Python. Then removing it once its been uploaded.

## Setting up the Bucket

* Firstly I created the Bucket and set it up on Amazon after creating an AWS account through Service then S3

* Once that was finished I created a user through IAM dashboard in Services.

* Copied the User ARN

* Reopened the S3 dashboard

* Now clicked the permissions tab to add Bucket Policy and added the following policy

* AWS is set to the User ARN. Also the Resource is set to the Bucket ARN.

```json {
    "Version": "2012-10-17",
    "Id": "Policy1488494182833",
    "Statement": [
        {
            "Sid": "Stmt1488493308547",
            "Effect": "Allow",
            "Principal": {
                "AWS": " "
            },
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:GetBucketLocation",
                "s3:Get*",
                "s3:Put*"
            ],
            "Resource": " "
        }
    ]
 } 
```

* Clicked the CORS configuration and add the following policy

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
  </CORSRule>
</CORSConfiguration>
```
* Reopened the IAM dashboard to view the your new user to add a New inline policy.

```json 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::*"
            ]
        }
    ]
}
```
