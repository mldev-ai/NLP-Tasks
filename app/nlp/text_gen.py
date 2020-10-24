from transformers import pipeline

text_generator = pipeline("text-generation")

def return_generated_text(context):
    return text_generator(context, max_length=100)
