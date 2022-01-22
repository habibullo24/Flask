from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("html1.html")


@app.route("/about/")
def about():
    return render_template("html2.html")


if __name__ == "__main__":
    app.run(debug=True)
