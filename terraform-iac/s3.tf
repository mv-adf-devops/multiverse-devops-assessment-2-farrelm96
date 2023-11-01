resource "aws_s3_bucket" "this" {
  bucket_prefix = "assessment-bucket-your-name"
  force_destroy = true

  tags = {
    Name = "multiverse"
  }
}

resource "aws_s3_bucket_acl" "this" {
  bucket = aws_s3_bucket.this.id
  acl    = "private"
  depends_on = [aws_s3_bucket_ownership_controls.s3_bucket_acl_ownership]
}

resource "aws_s3_bucket_ownership_controls" "s3_bucket_acl_ownership" {
    bucket = aws_s3_bucket.this.id
    rule {
        object_ownership = "ObjectWriter"
    }
}



resource "aws_s3_object" "this" {
  bucket = aws_s3_bucket.this.id
  key    = "results.csv"
  source = "${path.module}/results.csv"
  etag   = filemd5("${path.module}/results.csv")
}
