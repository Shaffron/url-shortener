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
        decoded = Base62.decode(url)
        shorten_url = manager.get('%s:%s' % (KEY.PREFIX.value, decoded))
        if not shorten_url:
            return render_template('/404.html')
        return redirect(shorten_url)

    def post(self, url):
        print(request)
        manager = UrlManager()
        index = manager.increase_total_counter()
        shorten = Base62.encode(index)
        payload = {
            'origin': url,
            'shorten': shorten,
            'created': datetime.now(tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%S %z')
        }
        response = manager.set('%s:%s' % (KEY.PREFIX.value, index), payload)
        if response:
            return shorten, 200
        else:
            'error', 500



class UrlListView(MethodView):
    def get(self):
        manager = UrlManager()
        shorten_urls = manager.get_all_shorten_urls()
        return render_template('/list.html', urls=shorten_urls)
