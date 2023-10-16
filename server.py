import datetime as dt
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length
import secrets
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField

secret_key = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)


class ContactForm(FlaskForm):
    name = StringField(label='Full Name', validators=[DataRequired()], render_kw={'placeholder': 'Will Smith'})
    email = EmailField(label='Enter email', validators=[DataRequired()], render_kw={'placeholder': 'myemail@gmail.com'})
    message = CKEditorField('message')
    submit = SubmitField(label='Submit')


@app.route('/')
def home():
    time = dt.datetime
    year = time.today().year
    return render_template('index.html', year=year)


@app.route('/connect', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    time = dt.datetime
    year = time.today().year
    if form.validate_on_submit():
        if request.method == 'POST':
            flash(message='Submitted Successfully')
            return redirect(url_for('contact'))
    return render_template('contact.html', year=year, form=form)


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
