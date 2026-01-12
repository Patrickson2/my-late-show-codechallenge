from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

#created the database configuration.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




if __name__ == '__main__':
    app.run(port=5555, debug=True)