#!/usr/bin/python3
""" Flask Application """
from models import storage
import os
from flask import Flask
from api.v1.views import app_views

# flask server environmental setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# app variable instance of Flask
app = Flask(__name__)

# Blueprint in api.v1.views
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """After each request this method is called to close sqlalchemy"""
    storage.close()

if __name__ == "__main__":
    """ Run main Flask App"""
    app.run(host = host, port = port)