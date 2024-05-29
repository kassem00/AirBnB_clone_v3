#!/usr/bin/python3
from . import app_views
from flask import jsonify
""" index view blueprint file """


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON indicating the status is OK."""
    return jsonify({'status': 'OK'})
