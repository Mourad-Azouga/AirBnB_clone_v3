#!/usr/bin/python3
"""
Still don't know the exact thing yet
"""

from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        whatever = {"status": "OK"}
        return jsonify(whatever)