from mongokit import Connection
from .models import models


def setup(app):

    conn = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

    db = conn[app.config['MONGODB_DBNAME']]

    # If user and password are given, authenticate
    if all(k in app.config for k in ('MONGODB_USERNAME', 'MONGODB_PASSWORD')):
        db.authenticate(app.config['MONGODB_USERNAME'], app.config['MONGODB_PASSWORD'])

    db.connection.register(models)

    return db
