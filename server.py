import datetime as dt
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
import secrets

secret_key = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

print(secret_key)


class Posts(FlaskForm):
    pass


@app.route('/')
def home():
    time = dt.datetime
    year = time.today().year
    return render_template('index.html', year=year)


@app.route('/connect', methods=['GET', 'POST'])
def contact():
    time = dt.datetime
    year = time.today().year
    if request.method == 'POST':
        print(request.form)
        flash(message='Submitted Successfully')
        return redirect(url_for('contact'))
    return render_template('contact.html', year=year)


@app.route('/projects')
def projects():
    time = dt.datetime
    year = time.today().year
    return render_template('projects.html', year=year)


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    time = dt.datetime
    year = time.today().year
    return render_template('blog.html', year=year)


if __name__ == '__main__':
    app.run(debug=True, port=400)
