from flask import Flask as flask
app = flask(__name__)

# Create main function that prints hello world
@app.route("/")
def hello_world():
    return "Hello World!"
