from app import app
from flask import request, jsonify, render_template
from app.nlp.sentiment import return_sentiment
from app.nlp.ques_ans import return_answer
from app.nlp.text_gen import return_generated_text

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sentiment", methods=["POST", "GET"])
def classify_sentiment():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)

    query = form_r["query"][0]
    result = return_sentiment(query)
    result[0]["query"] = query
    return jsonify(result)

@app.route("/squad", methods=["POST", "GET"])
def question_answering():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)

    question = form_r["question"][0]
    context = form_r["context"][0]

    result = return_answer(context, question)
    
    result["question"] = question
    result["context"] = context

    return jsonify(result)

@app.route("/gpt2", methods=["POST", "GET"])
def generate_text():
    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)

    context = form_r["context"][0]
    result = return_generated_text(context)
    
    result[0]["context"] = context

    return jsonify(result)