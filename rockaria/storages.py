from storages.backends.s3boto3 import S3Boto3Storage

# For serving static files from S3
class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"

# For serving media (uploaded) files from S3
class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False  # Keep multiple uploads with same filename
