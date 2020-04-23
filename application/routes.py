from flask import current_app as app
from . import db
from .data import getRecipe

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/banana")
def getit():
    return getRecipe("banana")