#!/usr/bin/python3
"""
Still don't know the exact thing yet
"""

from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', methods= ['GET'])
def status():
    if request.method == 'GET':
        return jsonify({'status':'OK'})