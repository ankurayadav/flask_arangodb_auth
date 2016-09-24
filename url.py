from flask_restful import Resource

from app import app, api

# Users resource
from auth.auth import auth
from auth.api import Users
from auth.api import get_auth_token


class HelloWorld(Resource):
    @auth.login_required
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(Users, '/api/users')
app.add_url_rule('/api/token', 'get_auth_token()', get_auth_token)


if __name__ == '__main__':
    app.run(debug=True)
