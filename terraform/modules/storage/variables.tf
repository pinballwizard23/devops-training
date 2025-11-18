variable bucket_name {
  description = "The name of the storage bucket"
  type        = string
}

variable environment {
  description = "The environment for the storage bucket"
  type        = string
}

variable aws_region {
  description = "The AWS region to create the S3 bucket in"
  type        = string
}