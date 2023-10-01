from flask import Flask, render_template, request, redirect, url_for, flash

# Create a Flask Instance

app = Flask(__name__)

# Create a route decorator
@app.route('/')
def home():
    # Render layout.html from templates folder
    return render_template('layout.html')