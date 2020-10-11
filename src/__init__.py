"""
The flask application package.
"""

from flask import Flask
from os import environ
from applicationinsights.requests import WSGIApplication
app = Flask(__name__, static_folder='html/static', template_folder='html/templates')
app.wsgi_app = WSGIApplication(environ.get('APPINSIGHTS_INSTRUMENTATIONKEY'), app.wsgi_app)
from src.pymod.endpoint.index import app
