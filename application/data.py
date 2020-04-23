import json
from . import db

def getRecipe(ingredient):

    myList = []

    for recipe in db:
        ingredients = db[recipe].get('ingredients')

        if ingredients is not None:
            if ingredient in str(ingredients):
                myList.append(db[recipe].get('title'))

    return str(myList)
