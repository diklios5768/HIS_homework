import os

from app import create_app

app = create_app()
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
