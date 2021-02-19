from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '930ccf70f3959160387f7e063494399d'

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Thank you for contacting me {form.name.data}! I\'ll be in touch! ', 'success')
        return redirect(url_for('home'))
    return render_template("index.html", form=form)

def contact():
    form = ContactForm()
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)