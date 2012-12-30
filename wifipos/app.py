from flask import Flask, request, jsonify, make_response
from mongokit import ValidationError, RequireFieldError

from db import setup as setup_db
import models


app = Flask(__name__)

# Load config
app.config.from_object('wifipos.default_settings')
app.config.from_envvar('WIFIPOS_SETTINGS')

# Connect to database
db = setup_db(app).connection


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['POST', 'GET']) # TODO remove get
def upload():
    sample = db.Wifisample()

    # param presence checking
    for k in ['x', 'y', 'z', 'level', 'essid', 'bssid']:
        if k not in request.form:
            return jsonify({ 'error': "missing parameter '%s'" % k })

    x, y, z = (float(request.form.get(p)) for p in ('x', 'y', 'z'))
    sample['pos'] = (x, y, z)
    sample['level'] = float(request.form.get('level'))
    sample['essid'] = request.form.get('essid')
    sample['bssid'] = request.form.get('bssid')
    sample['submitter_ip'] = request.remote_addr

    try:
        sample.save()
    except (ValidationError, RequireFieldError), e:
        return jsonify(error=e)
    else:
        return 'ok'


def main():
    # Start webserver
    app.run()
