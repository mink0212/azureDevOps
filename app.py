
from os import environ
from src import app

#app = Flask(__name__, static_folder='html/static', template_folder='html/templates')

if __name__ == "__main__":
    app.run(host='0.0.0.0')