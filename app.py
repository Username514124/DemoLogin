from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    user = request.args.get('user')
    print(user)
    if user == None:
        return render_template("index.html")
    elif user == "rob":
        return "Hello " + user
    else:
        return "User not recongised"