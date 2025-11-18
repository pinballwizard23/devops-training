## Buckets to create in AWS and Azure
module "buckets" {
  source = "./modules/storage"

  bucket_name   = "allmerged-gera"
  aws_region    = var.aws_region
  environment   = "Dev"
}