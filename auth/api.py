# from flask import abort, request
from flask_restful import reqparse, abort, Resource
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Users(Resource):
    def post(self):
        args = parser.parse_args()
        username = str(args['username'])
        password = str(args['password'])

        if username is None or password is None:
            return {"message": "missing arguments"}  # missing arguments
        if User.get({"username": username}).username is not None:
            return {"message": "user already exists"}  # existing user

        user = User.create(username=username, password=password)

        return {"username": user.username}
