
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify
from Pets import Pets

DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5431'
DB_NAME = 'animal_db'


CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(
    DATABASE,
    USER,
    PASSWORD,
    HOST,
    PORT,
    DB_NAME
)

app = Flask(__name__)


@app.route('/')
def root():
    return "root"


@app.route('/hello/<name>')
def hello(name):
    engine = create_engine(CONNECT_STR, connect_args={"application_name":"py_app"})
    session = sessionmaker(engine)()
    pets = session.query(Pets).filter(Pets.name==name).all()
    session.close()
    engine.dispose()
    return jsonify(pets)

if __name__ == "__main__":
    app.run()
