from flask import Flask
from libs.clients.celery_client import make_celery

# SECRET_KEY = 'TOP SECRET'

app = Flask(__name__)
celery = make_celery(app)
