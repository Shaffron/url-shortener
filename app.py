from flask import Flask

from compressor.views import IndexView, RedirectView


app = Flask(__name__)

# export settings
app.config.from_object('settings.default')


# router
app.add_url_rule(
    rule='/',
    view_func=IndexView.as_view('index')
)
app.add_url_rule(
    rule='/<url>',
    view_func=RedirectView.as_view('redirect')
)


if __name__ == '__main__':
    app.run()