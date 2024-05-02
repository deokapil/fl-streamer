# use flask application factory to build a new flask app
from flask import Flask
from dynaconf import FlaskDynaconf
from stapp.celeryd import celery_init_app
from stapp.celstreamer import views as celstream_view


def create_app() -> Flask:
    app = Flask(__name__)
    FlaskDynaconf(app, settings_files=["settings.toml", ".secrets.toml"])
    app.register_blueprint(celstream_view.bp)
    celery_init_app(app)
    return app
