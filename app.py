from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")

def index():

    return render_template("index.html")


@app.route("/gallery")

def gallery():

    return render_template("gallery.html")


@app.route("/specifications")

def specifications():

    return render_template("specifications.html")


if __name__ == "__main__":

    app.run(debug=True)
