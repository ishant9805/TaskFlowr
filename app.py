from flask import Flask

# Create a Flask Instance

app = Flask(__name__)

# Create a route decorator
@app.route('/')
def home():
    return "Hello World"