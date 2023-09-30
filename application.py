from flask import Flask, render_template, request, jsonify, redirect
from werkzeug.utils import secure_filename

application = Flask(__name__)


@application.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    application.run(debug=True)
