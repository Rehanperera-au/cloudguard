package cloudguard.require_encrypted_storage

# Require that storage buckets are encrypted at rest.
# This policy denies any storage resource that is not encrypted.
# The input should represent a storage bucket with fields 'kind', 'name', and 'encrypted'.

deny[msg] {
  input.kind == "Bucket"
  not input.encrypted
  msg := sprintf("Bucket %s is not encrypted at rest", [input.name])
}
