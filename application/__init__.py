from flask import Flask
import json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

with open("data1.json", "r") as file:
    db = json.load(file)

limiter = Limiter(key_func=get_remote_address)

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    #Initialize plugin
    limiter.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from . import data
        
        return app