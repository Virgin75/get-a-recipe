import json
from . import db
from random import randint


def getRecipes(*argv):

    myList = []

    for recipe in db:
        ingredients = db[recipe].get('ingredients')

        if ingredients is not None:

            if all(c in str(ingredients) for c in argv):
                
                myList.append(db[recipe])

    return myList

def getRandom():

    randomIndex = list(db)[randint(0, len(db))]

    return db[randomIndex]
