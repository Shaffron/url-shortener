from redis import Redis
from flask import current_app



class RedisClient:
    def __init__(self):
        self.host = current_app.config.get('REDIS_HOST', 'localhost')
        self.password = current_app.config.get('REDIS_PASSWORD', None)
        self.port = current_app.config.get('REDIS_PASSWORD', 6379)
        self.db = current_app.config.get('REDIS_DB', 0)
        self.redis = self.get_redis_client()

    def get_redis_client(self):
        client = Redis(
            host=self.host,
            password=self.password,
            port=self.port,
            db=self.db
        )
        return client

    def get(self, key):
        response = self.redis.get(key)
        return response

    def set(self, key, value):
        response = self.redis.set(key, value, nx=True)
        return response

    def increment(self):
        response = self.redis.incr('counter')
        return response
