from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/papers")
def papers():
    return render_template("papers.html")

@app.route("/teaching")
def teaching():
    return render_template("teaching.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/extra")
def extrcrc():
    return render_template("extra.html")

if __name__ == "__main__":
    app.run(debug=True)