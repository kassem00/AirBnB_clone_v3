#!/usr/bin/python3
""" index view blueprint file """
from . import app_views
from flask import jsonify
from json import loads
from models import storage
""" index view blueprint file """


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON indicating the status is OK."""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def count():
    '''retrieves the number of each objects by type'''
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)
