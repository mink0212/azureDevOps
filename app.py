
from flask import Flask, render_template, url_for

from pymod.endpoint.index import index_fnc

app = Flask(__name__, static_folder='html/static', template_folder='html/templates')


@app.route('/')
@app.route('/index')
def index():
    return index_fnc()

if __name__ == "__main__":
    app.run()