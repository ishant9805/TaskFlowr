from flask import Flask, render_template, request, redirect, url_for, flash

# Create a Flask Instance

# Edited by Ishant

app = Flask(__name__)

# Create a route decorator
@app.route('/')
def home():
    # Render layout.html from templates folder
    return render_template('tasks.html')

# now render feature.html
@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/about')
def about():
    return render_template('about.html')
