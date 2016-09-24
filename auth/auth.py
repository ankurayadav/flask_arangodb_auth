from flask_httpauth import HTTPBasicAuth
from models import User, check_hashed_password

from app import g

auth = HTTPBasicAuth()


@auth.verify_password
# Function to verify user password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.get({"username": username_or_token})
        if not user.username or not check_hashed_password(password, user.password_hash):
            return False
    g.user = user
    return True
