#!/usr/bin/python3
from flask import Blueprint
""" blueprint init """


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
    from .index import *
