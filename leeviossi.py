from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/form", methods=["POST", "GET"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    comment = request.form.get("comment")

    message = ("From: "+name+" <"+email+"> \nmessage: "+comment)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("leevi.devtraining@gmail.com", "dypcen-Hecru4-qatjeb") #replace with environment/os var
    server.sendmail("leevi.devtraining@gmail.com", "leevi.ossi@hotmail.com", message)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)