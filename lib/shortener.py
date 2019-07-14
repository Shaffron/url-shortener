from zlib import crc32
from uuid import uuid4

from lib.base62 import Base62



class UrlShortener:
    @classmethod
    def get_url(cls):
        uid = cls.get_uuid()
        hash_string = cls.hash_uuid(uid)
        shorten_url = cls.encode_base62(hash_string)
        return shorten_url

    def get_uuid(self):
        return str(uuid4())

    def hash_uuid(self, uid):
        uid = uid.encode('utf-8')
        hash_string = crc32(uid)
        return hash_string

    def encode_base62(self, hash_string):
        base62 = Base62.encode(hash_string)
        return base62
