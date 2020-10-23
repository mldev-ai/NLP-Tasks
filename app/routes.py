from app import app
from flask import request, jsonify, render_template
from app.nlp.sentiment import return_sentiment

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sentiment", methods=["POST", "GET"])
def classify_sentiment():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)
    # print("form_r", form_r)

    query = form_r["query"][0]
    result = return_sentiment(query)
    # print(result)
    result[0]["query"] = query
    return jsonify(result)