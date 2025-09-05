# AI prompts to identify common cloud misconfigurations.
# Each entry describes a type of misconfiguration and provides a templated prompt.

PROMPTS = {
    "public_s3_bucket": (
        "You are a cloud security analyst. Identify any security misconfigurations in the following S3 bucket policy. "
        "Look for public read or write access, wildcard principals, and missing encryption requirements.\n\n{policy}"
    ),
    "open_security_group": (
        "You are reviewing a cloud security group. Check if there are any rules allowing unrestricted inbound access "
        "(e.g., 0.0.0.0/0 or ::/0) to sensitive ports. Summarize any misconfigurations you find.\n\n{security_group}"
    ),
    "unencrypted_ebs_volume": (
        "Determine if the following AWS EBS volume configuration is encrypted at rest. "
        "If encryption is disabled, explain why this is a security risk and suggest remediation.\n\n{ebs_config}"
    ),
    "overly_permissive_iam_policy": (
        "Analyze the IAM policy below. Identify any statements that grant wildcard (*) permissions or full access. "
        "Explain why this is insecure and how to restrict permissions.\n\n{iam_policy}"
    ),
    "public_rds_instance": (
        "Review the following RDS instance configuration. Check if the instance is publicly accessible "
        "and if so, explain the risks and how to restrict access.\n\n{rds_config}"
    )
}
