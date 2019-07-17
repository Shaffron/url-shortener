import json
from datetime import datetime, timezone

from flask import render_template, request, redirect
from flask.views import MethodView

from compressor.constants import KEY
from compressor.manager import UrlManager
from lib.base62 import Base62



class IndexView(MethodView):
    def get(self):
        return render_template('/index.html')



class RedirectView(MethodView):
    def get(self, url):
        manager = UrlManager()
        response = manager.get('%s:%s' % (KEY.PREFIX.value, url))
        if not response:
            return render_template('/404.html')
        else:
            response = json.loads(response)
            return redirect('%s://%s' % (response['protocol'], response['origin']))



class UrlGeneratorView(MethodView):
    def __init__(self, *args, **kwargs):
        self.manager = UrlManager()
        self.category = request.form.get('category')
        self.protocol = request.form.get('protocol')
        self.origin = request.form.get('origin')

    def post(self):
        index, shorten = self.get_shorten_url()

        payload = {
            'index': index,
            'protocol': self.protocol,
            'origin': self.origin,
            'shorten': shorten,
            'created': datetime.now(tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%S %z')
        }

        response = self.insert_shorten_url(payload)
        if response:
            return { 'url': '%s%s' % (request.host_url, shorten) }, 200

    def is_exist(self, shorten):
        return self.manager.get('%s:%s' % (KEY.PREFIX.value, shorten)) is not None

    def insert_shorten_url(self, payload):
        return self.manager.set('%s:%s' % (KEY.PREFIX.value, payload['shorten']), payload)

    def get_shorten_url(self):
        index = self.manager.increase_total_counter()

        if self.category == 'specific' and 'specific' in request.form:
            specified = True
            shorten = request.form.get('specific')
        else:
            shorten = Base62.encode(index)

        # check key collision
        if (
            shorten in ['list', 'generate'] or
            self.manager.get('%s:%s' % (KEY.PREFIX.value, shorten)) is not None
        ):
            if specified:
                return { 'message': '[%s] already in use' % shorten }, 409
            else:
                is_exist = self.is_exist(shorten)
                while not is_exist:
                    index = self.manager.increase_total_counter()
                    shorten = Base62.encode(index)
                    is_exist = self.is_exist(shorten)
        return index, shorten



class UrlListView(MethodView):
    def get(self):
        manager = UrlManager()
        urls = manager.get_all_shorten_urls()
        return render_template('/list.html', urls=urls)
