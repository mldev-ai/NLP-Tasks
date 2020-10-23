from transformers import pipeline

nlp = pipeline("question-answering")

def return_answer(context, question):

    return nlp(question=question, context=context)

# context = r"""
# Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
# question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
# a model on a SQuAD task, you may leverage the `run_squad.py`.
# """

# print(nlp(question="What is extractive question answering?", context=context))
# print(nlp(question="What is a good example of a question answering dataset?", context=context))
