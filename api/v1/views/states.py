#!/usr/bin/python3
"""
Handles all the state related methods
"""
from models import storage
from flask import abort, jsonify, request
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """
    Retrieves and works on states without specifying the id
    """
    if request.method == 'GET':
        all_states = storage.all('State')
        all_states = list(obj.to_json() for obj in all_states.values())
        return jsonify(all_states)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        return jsonify(request.to_json()), 201

@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def states_id(state_id = None):
    """
    Works on states with a specified ID
    """
    # Checks if the state actually exists
    state_object = storage.get('State', state_id)
    if state_object == None:
        abort(404, 'Not found')
    
    # If it doesn't it'll abord 404, if it does it'll turn it to json
    if request.method == 'GET':
        return jsonify(state_object.to_json())
    
    # Deletes a state
    if request.method == 'DELETE':
        state_object.delete()
        del state_object
        return jsonify({})
    
    # Makes a json request to update a state
    if request.method == 'PUT':
        json_request = request.get_json()
        if json_request == None:
            abort(400, 'Not a JSON')
        state_object.bm_update(json_request)
        return jsonify(state_object.to_json())
