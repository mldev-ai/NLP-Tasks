from transformers import pipeline

nlp = pipeline("sentiment-analysis")

def return_sentiment(query):
    return nlp(query)
