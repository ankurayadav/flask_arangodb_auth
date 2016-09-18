# python
from pyArango.connection import Connection
from passlib.apps import custom_app_context as pwd_context

import settings

# Creating connection with arangoDB
conn = Connection(arangoURL=settings.ARANGODB_HOST, username=settings.ARANGODB_USERNAME, password=settings.ARANGODB_PASSWORD)
# Selecting database
db = conn[settings.ARANGODB_DATABASE]
# Selecting collections for auth users
collection = db["users"]


class User(object):
    # Information stored in users collection.
    key = None
    username = None
    password_hash = None

    # Function to new user in users collection.
    @classmethod
    def create(cls, username, password):
        doc = collection.createDocument()
        doc["username"] = username
        password_hash = hash_password(password)
        doc["password_hash"] = password_hash
        doc.save()

        new_user = User()
        new_user.key = doc._key
        new_user.username = username
        new_user.password_hash = password_hash
        return new_user

    @classmethod
    def get(cls, query_dict):
        query = collection.fetchFirstExample(query_dict)

        ret_user = User()

        for record in query.result:
            ret_user.key = record["_key"]
            ret_user.username = record["username"]
            ret_user.password_hash = record["password_hash"]

        return ret_user

# Function to generate password_hash for given password
def hash_password(password):
    password_hash = pwd_context.encrypt(password)
    return password_hash

# Function to verify password based on password_hash
def check_hashed_password(password, password_hash):
    return pwd_context.verify(password, password_hash)

