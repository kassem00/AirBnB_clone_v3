from flask import Blueprint
""" doc_me """


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from .index import *
