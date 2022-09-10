from turtle import title
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = "Login con Flask."
    return render_template("index.html", title=title)



if __name__ == "__main__":
    app.run(debug=True)