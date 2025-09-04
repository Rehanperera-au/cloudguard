package cloudguard.aws

# Deny public S3 buckets

# This policy denies creation of S3 buckets that are publicly accessible.
# It expects an input structure with resource_type, configuration and resource_name fields.

deny[msg] {
  input.resource_type == "aws_s3_bucket"
  input.configuration.public == true
  msg := sprintf("S3 bucket %s is publicly accessible; public buckets are not allowed.", [input.resource_name])
}
