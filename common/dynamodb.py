import os
import boto3


class DatabaseHandler:
    def __init__(self):
        self._dynamodb = boto3.resource('dynamodb')
        self._table = self._dynamodb.Table(os.environ['TABLE_NAME'])

    def is_site(self, pointer):
        return False

    def is_collection(self, pointer):
        return False