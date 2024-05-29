#!/usr/bin/python3
""" index view blueprint file """
from . import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON indicating the status is OK."""
    return jsonify(status="OK")
