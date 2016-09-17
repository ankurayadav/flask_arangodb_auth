# python
from pyArango.connection import *

import settings

conn = Connection(username=settings.ARANGODB_USERNAME, password=settings.ARANGODB_PASSWORD)
db = conn["mydatabase"]

# Creating collection for auth users
collection = db.createCollection(name="users")