flask_arangodb_auth
===================

This project contains auth code for flask using arangodb as backend.
--------------------------------------------------------------------

This project contains two branches:
1. **simple_auth**: Contains simple auth framework for username and password based login using flask-restfull
                    and arangodb as the backend.
2. **master**; This contains token based auth using flask-restful and arangodb as the backend.

###Setup Steps
1. Make a database of your in arangodb and put it in settings.py as:
<pre><code>
ARANGODB_DATABASE="mydatabase"
</pre></code>
2. Run the migration for making users collection:
<pre><code>
$> python migrate_collections.py
</pre></code>
3. Run server to test it.
<pre><code>
$> python url.py
</pre></code>
4. Open a new terminal.
5. Create a user.
<pre><code>
$> curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user","password":"pass"}' http://127.0.0.1:5000/api/users
</pre></code>
6. Try to get access token for that user.
<pre><code>
$> curl -u user:pass -i -X GET http://127.0.0.1:5000/api/token
</pre></code>
7. Now you will get an auth token. You can use that auth token to access other resources like:
<pre><code>
$> curl -u your-auth-token:unused -i -X GET http://127.0.0.1:5000/
</pre></code>
8. You should get hello world in response.