import os

import flask
import workos

# Flask Setup
DEBUG = False
app = flask.Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# WorkOS Setup
workos.api_key = os.getenv('WORKOS_API_KEY')
workos.base_api_url = 'http://localhost:7000/' if DEBUG else workos.base_api_url
DIRECTORY = os.getenv('SCIM_ENDPOINT_ID')


@app.route('/users')
def directory_users():
    users = workos.client.directory_sync.list_users(directory=DIRECTORY)
    return users


@app.route('/groups')
def directory_groups():
    groups = workos.client.directory_sync.list_groups(directory=DIRECTORY)
    return groups
