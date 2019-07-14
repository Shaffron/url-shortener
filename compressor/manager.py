import json

from compressor.constants import KEY
from lib.redis import RedisClient



class UrlManager(RedisClient):
    def get(self, key):
        response = self.redis.get(key)
        return response

    def set(self, key, payload):
        payload = json.dumps(payload)
        response = self.redis.set(key, payload, nx=True)
        if response:
            self.add_to_member(payload)
        return response

    def increase_total_counter(self):
        response = self.redis.incr(KEY.COUNTER.value)
        return response

    def add_to_member(self, payload):
        response = self.redis.sadd(KEY.ALL_URLS.value, payload)
        return response

    def get_all_shorten_urls(self):
        urls = self.redis.smembers(KEY.ALL_URLS.value)
        response = [json.loads(url) for url in urls]
        return response
