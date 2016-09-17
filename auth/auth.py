from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

from models import User, check_hashed_password

@auth.verify_password
# Function to verify user password
def verify_password(username, password):
    user = User.get({"username": username})
    print user.username
    if not user.username or not check_hashed_password(password, user.password_hash):
        return False
    return True