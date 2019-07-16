from flask import Flask

app = Flask(__name__)

@app.route("/")
def greeting():
    return "hello"

if __name__ == "__main__":
    app.run()