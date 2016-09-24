from flask import Flask, g
from flask_restful import Api
app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_auth'
api = Api(app)
