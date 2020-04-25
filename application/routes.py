from flask import request, jsonify, current_app as app
from . import db, limiter
from .data import getRecipes, getRandom

#Get a random recipe
@app.route("/api/random")
@limiter.limit("300/day;50/minute")
def getRandomrecipe():

    return jsonify(getRandom())

#Get a list of recipes containing the requested ingredients
#Route example '/api/recipes?1=banana&2=chocolate&3=strawberry'
@app.route("/api/recipes")
@limiter.limit("150/day;15/minute")
def getMatchingRecipes():

    ingredients = []
    for ingredient in range(1, len(request.args) + 1):
        ingredients.append(request.args.get(str(ingredient)))

    data = getRecipes(*ingredients)

    response = {"Number of results": len(data),
                "recipes": data}

    return jsonify(response)

#Page not found
@app.errorhandler(404) 
def not_found(e):

    resp = {"error": str(e)}
    return jsonify(resp)


#Too many requests
@app.errorhandler(429)
def ratelimit_handler(e):

    return jsonify(error="ratelimit exceeded %s" % e.description)