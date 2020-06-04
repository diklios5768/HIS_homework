import click
import os
from flask import Flask

from app.models import db
from app.models.base import *
from app.models.doctor import *
from app.models.hospital import *
from app.models.medical_treatment import *
from app.models.user import *
from . import routes


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'secret string')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
                                                      'sqlite:///' + os.path.join(app.root_path, 'data.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """
        Initialized database。
        :return:
        """
        if drop:
            click.confirm('This operation will delete the database,do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database!')

    db.init_app(app)
    routes.init_app(app)
    return app
