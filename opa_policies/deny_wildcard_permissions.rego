package cloudguard.deny_wildcard_permissions

# Deny IAM roles or policies that grant wildcard (*) privileges.
# This policy checks for wildcard actions or resources and returns a denial message.
# The input should be a simplified representation of an IAM policy with
# 'actions' and 'resources' arrays.

deny[msg] {
  input.actions[_] == "*"
  msg := "Wildcard actions are not allowed in IAM policies."
}

deny[msg] {
  input.resources[_] == "*"
  msg := "Wildcard resources are not allowed in IAM policies."
}
