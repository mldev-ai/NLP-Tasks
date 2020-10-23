from transformers import pipeline

text_generator = pipeline("text-generation")

def return_generated_text(context):
    return text_generator(context, max_length=50)

# print(text_generator("As far as I am concerned, I will", max_length=50))
