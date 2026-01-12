from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import *

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=5555, debug=True)