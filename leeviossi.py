from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ContactForm
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '930ccf70f3959160387f7e063494399d'
app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Thank you for contacting me {form.name.data}! I\'ll be in touch! ', 'success')
        name = form.name.data
        email = form.email.data
        message = form.message.data
        send_mail(name, email, message)
        return redirect(url_for('home'))
    return render_template("index.html", form=form)

def contact():
    form = ContactForm()
    return render_template('index.html', form=form)

def send_mail(name, email, message):
    msg = Message(name, sender=email, recipients=['leevi.ossi@hotmail.com'])
    msg.body = message
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug=True)