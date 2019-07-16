import pytest
from fakeredis import FakeStrictRedis

from app import app



class TestViews:
    @pytest.fixture(scope='class')
    def app(self):
        return app.test_client()

    def test_index_view(self, app):
        response = app.get('/')
        assert response.mimetype == 'text/html'
        assert response.status_code == 200

    def test_url_list_view(self, mocker, app):
        mocker.patch('lib.redis.Redis', return_value=FakeStrictRedis())
        response = app.get('/list')
        assert response.mimetype == 'text/html'
        assert response.status_code == 200

    def test_not_found_view(self, mocker, app):
        mocker.patch('lib.redis.Redis', return_value=FakeStrictRedis())
        response = app.get('/not_exist_shorten_url')
        # 404 Error Page
        assert response.mimetype == 'text/html'
        assert response.status_code == 200

    def test_url_generate_view(self, mocker, app):
        mocker.patch('lib.redis.Redis', return_value=FakeStrictRedis())
        payload = {
            'category': 'auto',
            'protocol': 'http',
            'origin': 'www.google.com'
        }
        response = app.post('/generate', data=payload)
        assert 'url' in response.get_json()
        assert response.mimetype == 'application/json'
        assert response.status_code == 200

        url = response.get_json()['url']
        shorten = url.split('/')[-1]
        payload = {
            'category': 'specific',
            'protocol': 'http',
            'origin': 'www.google.com',
            'specific': shorten
        }
        response = app.post('/generate', data=payload)
        assert response.mimetype == 'application/json'
        assert response.status_code == 409

        wanted = 'my-shorten-url'
        payload = {
            'category': 'specific',
            'protocol': 'http',
            'origin': 'www.google.com',
            'specific': wanted
        }
        response = app.post('/generate', data=payload)
        assert 'url' in response.get_json()
        url = response.get_json()['url']
        shorten = url.split('/')[-1]
        assert response.mimetype == 'application/json'
        assert response.status_code == 200
        assert shorten == wanted

    def test_redirect_view(self, mocker, app):
        mocker.patch('lib.redis.Redis', return_value=FakeStrictRedis())
        payload = {
            'category': 'auto',
            'protocol': 'http',
            'origin': 'www.google.com'
        }
        response = app.post('/generate', data=payload)
        url = response.get_json()['url']
        shorten = url.split('/')[-1]
        redirect = app.get('/%s' % shorten)
        location = redirect.headers.get('Location')
        assert redirect.status_code == 302
        assert location == '%s://%s' % (payload['protocol'], payload['origin'])
