variable aws_region {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-west-2"
}

variable sso-profile {
  description = "The AWS SSO profile to use for authentication"
  type        = string
  default     = "sso-devops"
}