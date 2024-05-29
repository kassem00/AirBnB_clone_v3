#!/usr/bin/python3
from . import app_views
from flask import jsonify
""" doc_me """


@app_views.route('/status', methods=['GET'])
def status():
    """Return a JSON indicating the status is OK."""
    return jsonify(status="OK")
