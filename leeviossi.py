from flask import Flask, render_template, request, redirect, url_for, flash
from flask_scss import Scss
from forms import ContactForm
from flask_mail import Mail, Message
import os

app = Flask(__name__)
Scss(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_FLASK_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    skills = [
        'html', 'css', 'javascript', 'python', 'java', 'flask', 'django', 'sass', 
        'sql databases', 'git', 'linode', 'cisco ccna'
        ]
    if form.validate_on_submit():
        flash(f'Thank you for contacting me {form.name.data}! I\'ll be in touch! ', 'success')
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(f'Contact from {email}', sender=email, recipients=['leevi.ossi@gmail.com'])
        msg.body = message
        mail.send(msg)
        return redirect(url_for('home'))
    return render_template("index.html", form=form, skills=skills)

@app.route("/fi", methods=["GET", "POST"])
def homefi():
    form = ContactForm()
    skills = [
        'html', 'css', 'javascript', 'python', 'java', 'flask', 'django', 'sass', 
        'sql databases', 'git', 'linode', 'cisco ccna'
        ]
    if form.validate_on_submit():
        flash(f'Kiitos kun otit minuun yhteyttä {form.name.data}! Olen yhteydessä sinuun mahdollisimman pian! ', 'success')
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(f'Contact from {email}', sender=email, recipients=['leevi.ossi@gmail.com'])
        msg.body = message
        mail.send(msg)
        return redirect(url_for('homefi'))
    return render_template("./fi/index.html", form=form, skills=skills)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)