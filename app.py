from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import *

#creating a constructor for this flask class application
app = Flask(__name__)

#created the database configuration.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initializing the database with the flask app
db.init_app(app)

@app.route('/')
def home():
    return '<h1> Welcome to my late show app</h1>'






if __name__ == '__main__':
    app.run(port=5555, debug=True)