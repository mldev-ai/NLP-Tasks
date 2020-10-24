# NLP-Tasks

Various NLP tasks using Huggingface and Flask. Right now, the app supports only three tasks:

1. **Sentiment Analysis**: Identify if the sentence's sentiment is _Positive_ or _Negative_.

2. **Extractive Question Answering**: For a given _Context_ paragraph ask a _Question_. You should get an _Answer_ from the paragraph.

3. **Text Generation**: Provide a _Context_ (start of a sentence) and let the AI complete your story.

Plan is to include more tasks in future. Hugginface's `transformers` library makes these things very easy to do. 

Contributions are most welcome.

## Usage

1. Clone the repo: 
    `git clone https://github.com/mldev-ai/NLP-Tasks.git`

2. Navigate into the downloaded repo:
    `cd NLP-Tasks`

3. Install the required dependencies:
    `pip install -r requirements.txt`

4. Run the flask-app:

    * Windows Powershell:
    
        `$env:FLASK_APP="app.py"`
    
        `flask run`

    * Linux:
        
        `export FLASK_APP=app.py`
        
        `flask run`

## Notes

* The app is tested on Windows only. If you're using other OS and encounter any problem, please raise an issue.

* I tried deploying the app to Heroku in two ways, got problem in both:

    * Using Docker: dependecy issues with `transformers` library.

    * Direct Flask with git: size limit increased because of the `transformers` library's requirements, which are, some pre-trained models and full `PyTorch` library.

## Contributions

Right now, the most important contribution that can be made to this repo are:

1. Reduce the inference time, currently its too high (around 10 seconds for question answering task).

2. Deploy the app to any hosting site such as heroku, AWS, or Azure.

3. Add more NLP tasks to the app.

4. BTW, if someone can make nice UI using CSS or JS. That would be a huge plus. :)

## Acknowledgement

[Huggingface's transformers](https://huggingface.co/transformers/) library has revolutionised the way state-of-the-art NLP models are being used in real-world. Without, this library, the app made here would have taken tremendous amount of time (compared to what it took now).
