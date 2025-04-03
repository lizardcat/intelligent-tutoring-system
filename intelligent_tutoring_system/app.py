# def create_app():
#     # Your app initialization code here
#     pass
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Welcome to the Home Page!"  # Or render a template

    return app