from flask import Flask
from flask_restful import Resource, Api

from auth.auth import auth

# Users resource
from auth.api import Users

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    @auth.login_required
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(Users, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)
