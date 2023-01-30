from flask import Flask, render_template, redirect, url_for
from flask import request
from cron import parse
from nonst import macro
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == 'POST':
        data = request.form.get('cron')
        if len(data.split()) == 5:
            message = parse(data)
        elif data.startswith('@'):
            message = macro(data)
        else:
            message = 'Wrong input! It must consist 5 arguments'
    else:
        return redirect(url_for('index'))
    if type(message) == str:
        return redirect(url_for('valid', message=message))
    return render_template('result.html', message=message)


@app.route('/valid/<message>/')
def valid(message):
    return render_template('valid.html', message=message)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
