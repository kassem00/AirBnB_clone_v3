#!/usr/bin/python3
"""Flask application setup with teardown and main entry point."""

from flask import Flask
from api.v1.views import app_views
from models import storage
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_after_each_req(self):
    """Ensure resources are freed when the app context is torn down."""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    port = int(port)
    app.run(host=host, port=port, threaded=True, debug=True)
