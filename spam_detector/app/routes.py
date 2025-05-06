from flask import Blueprint, render_template, request
from .model import predict_spam

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        message = request.form['message']
        result = predict_spam(message)
    return render_template('index.html', result=result)
