from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World. It is me, Baran!"

@app.route("/oauth/callback")
def callback():
    return "Oauth Callback URL"

if __name__ == "__main__":
    app.run(debug=True)

