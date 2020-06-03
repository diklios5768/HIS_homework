from flask import Flask


def create_app():
    from . import routes
    from app.models import db
    app = Flask(__name__)
    db.init_app(app)
    routes.init_app(app)
    return app
