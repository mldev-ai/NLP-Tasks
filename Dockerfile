FROM python:3.7-stretch

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# CMD ["python", "main.py"]
CMD gunicorn --bind 0.0.0.0:$PORT main
