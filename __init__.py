from flask import Flask, render_template, request, redirect, url_for, flash
import os

def create_app():
    # Create a Flask Instance
    app = Flask(__name__, instance_relative_config=True)
    # Config secret key
    app.config.from_mapping(
        SECRET_KEY='IamConqKiller',
        DATABASE = os.path.join(app.instance_path, 'taskflowr.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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
    
    from . import database
    database.init_app(app)
    
    return app


if __name__ == '__main__':
    create_app().run(debug=True)