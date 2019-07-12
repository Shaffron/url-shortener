from flask.views import MethodView
from lib.redis import RedisClient



class RedisMixin(MethodView):
    def __init__(self, *args, **kwargs):
        self.redis = RedisClient()
        return super().__init__(*args, **kwargs)
