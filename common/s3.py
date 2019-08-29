import os
import boto3

class StorageHandler:
    def __init__(self):
        self._s3 = boto3.resource('s3')
        self._content_bucket = self._s3.Bucket(os.environ['CONTENT_BUCKET'])

    def get_content(pointer):
        return pointer

    def set_content(content):
        return content