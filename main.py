import datetime as dt
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
import secrets
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from smtplib import SMTP
import html
import os
import base64

secret_key = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)


class ContactForm(FlaskForm):
    name = StringField(label='Full Name', validators=[DataRequired()], render_kw={'placeholder': 'Will Smith'})
    email = EmailField(label='Enter email', validators=[DataRequired()], render_kw={'placeholder': 'myemail@gmail.com'})
    message = TextAreaField('message', validators=[DataRequired()],
                            render_kw={'placeholder': 'Type your message here...', 'class': 'custom-text-field'})
    submit = SubmitField(label='Submit')


# creating a simple tag remover.
def tag_remover(text):
    new_text = text.split('>')
    new_text = new_text[1].split('<')
    clean_text = new_text[0]
    return clean_text


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
            user_email = form.data.get('email')
            user_name = form.data.get('name')
            user_message = form.data.get('message')
            send_email(name=user_name, email=user_email, message=user_message)
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


def send_email(name, email, message):
    sender_email = os.environ.get('S_EMAIL')
    sender_password = os.environ.get('PASSWORD')
    receiver_email = os.environ.get('R_EMAIL')
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=(f"Subject:New Message from pleymate.com\n\n"
                                 f"Sender: {name}\n"
                                 f"Email: {email}\n"
                                 f"\nMessage: {message}").encode('utf8'))
        connection.close()


if __name__ == '__main__':
    app.run(debug=False)
