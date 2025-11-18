resource "aws_s3_bucket" "allmerged-gera" {
  bucket = "allmerged-gera"

  tags = {
    Name        = var.bucket_name
    Environment = var.environment
  }
}