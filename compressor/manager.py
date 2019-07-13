from compressor.constants import KEY
from lib.redis import RedisClient



class UrlManager(RedisClient):
    def get(self, key):
        response = self.redis.get(key)
        return response

    def set(self, key, url):
        response = self.redis.set(key, url, nx=True)
        if response:
            self.add_to_member(url)
        return response

    def increase_total_counter(self):
        response = self.redis.incr(KEY.COUNTER.value)
        return response

    def add_to_member(self, url):
        response = self.redis.sadd(KEY.ALL_URLS.value, url)
        return response

    def get_all_shorten_urls(self):
        response = self.redis.smembers(KEY.ALL_URLS.value)
        return response
