from transformers import pipeline

nlp = pipeline("question-answering")

def return_answer(context, question):
    return nlp(question=question, context=context)
