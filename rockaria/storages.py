from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'static'
    default_acl = 'public-read'

class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'media'
    default_acl = 'public-read'


    from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'static'
    default_acl = 'public-read'
    
    def __init__(self, *args, **kwargs):
        print(f"DEBUG: StaticStorage initialized with bucket: {self.bucket_name}")
        super().__init__(*args, **kwargs)

class MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = 'media'
    default_acl = 'public-read'
