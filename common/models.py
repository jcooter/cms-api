from datetime import datetime
from uuid import uuid1 as uuid

from .s3 import StorageHandler as storage
from .dynamodb import DatabaseHandler as database

class Post:
    def __init__(self):
        self._id = uuid()
        self._type = 'Post'
        self._create_timestamp = datetime.utcnow()
        self._site = []
        self._collection = []
        self._published = False
        self._author = ""
        self._title = ""
        self._slug = ""
        self._content_type = "text/markdown"
        self._content = ""

    @property
    def id(self):
        return self._id

    @property
    def create_timestamp(self):
        return self._create_timestamp

    @property
    def sites(self):
        return self._site

    @sites.setter
    def sites(self, value):
        if isinstance(value, list):
            for instance in value:
                if not database.is_site(instance):
                    raise ValueError('The provided site {} does not exist' % instance)
            self._site = value
        elif value:
            self._site = [ value ]
        else:
            raise TypeError('Unknown value for sites property')

    @property
    def collections(self):
        return self._collection

    @collections.setter
    def collections(self, value):
        if isinstance(value, list):
            for instance in value:
                if not database.is_collection(instance):
                    raise ValueError('The provided collection {} does not exist' % instance)
            self._collection = value
        elif value:
            self._collection = [ value ]
        else:
            raise TypeError('Unknown value for collections property')

    @property
    def is_published(self):
        return self._published

    @is_published.setter
    def is_published(self, value):
        if value:
            self._published = True
        else:
            self._published = False

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError('Unsupported Type for author attribute')
        if len(value) <= 64:
            self._author = value
        else:
            raise ValueError('Author max length is 64 characters')

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError('Unsupported Type for title attribute')
        if len(value) <= 256:
            self._author = value
        else:
            raise ValueError('Title max length is 256 characters')

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, value):
        if not isinstance(value, str):
            raise TypeError('Unsupported Type for slug attribute')
        if len(value) <= 32:
            self._slug = value
        else:
            raise ValueError('Slug max length is 32 characters')

    @property
    def content_type(self):
        return self._content_type

    @property
    def content(self):
        storage.get_content(self._content)

    @content.setter
    def content(self, value):
        # TODO: Validate markdown syntax
        storage.set_content(value)