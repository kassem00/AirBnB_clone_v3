from api.v1.views import app_views
from flask import Flask
from models import storage
import os
"""Flask application setup with teardown and main entry point."""


app = Flask(__name__)


@app.teardown_appcontext
def close_after_each_req(exception=None):
    """Ensure resources are freed when the app context is torn down."""
    storage.close()


if "__main__" == __name__:
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    port = int(port)
    app.run(host=host, port=port, threaded=True)
