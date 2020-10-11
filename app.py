
from flask import Flask, render_template, url_for

from src import app

#app = Flask(__name__, static_folder='html/static', template_folder='html/templates')

if __name__ == "__main__":
    app.run()