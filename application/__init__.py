from flask import Flask
import json

with open("data1.json", "r") as file:
    db = json.load(file)
    

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Include our Routes
        from . import routes
        from . import data
        
        return app