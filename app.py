from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        un = request.form['un']
        pw = request.form["pw"]
        if un =="rob" and pw =="321":
            return "Hello " + un
        elif un == "rob" and pw ==(""):
            return (un + " Please enter a password")
        elif un == "rob":
            return "Incorrect Password"
        else:
            return "User not recongised"
