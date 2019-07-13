from flask import render_template, request, redirect
from flask.views import MethodView

from lib.base62 import Base62
from lib.mixins import RedisMixin



class IndexView(MethodView):
    def get(self):
        return render_template('/index.html')



class RedirectView(RedisMixin, MethodView):
    def get(self, url):
        return redirect('https://www.google.com')