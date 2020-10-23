from app import app
from flask import request, jsonify, render_template
from app.nlp.sentiment import return_sentiment

@app.route("/")
def hello():
    return jsonify({"Hello":"World"})

@app.route("/sentiment")
def classify_sentiment():
    result = return_sentiment("I love you!")
    return jsonify(result)