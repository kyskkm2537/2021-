from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(
        "hello.html",
        title = "Hello, Flask!")

@app.route("/first")
def first():
    return render_template("first.html", title = "First Page111111111111111")

@app.route("/second")
def second():
    return render_template("second.html", title = "Second Page2222222222")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

