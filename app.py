from zenora import APIClient
from flask import Flask, render_template, request
from config import *

app = Flask(__name__)
client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

@app.route("/")
def home():
    return render_template("index.html", oauth_url=OAUTH_URL)

@app.route("/oauth/callback")
def callback():
    code = request.args['code']
    oauth_response = client.oauth.get_access_token(code=code, redirect_uri=REDIRECT_URI)
    return oauth_response.access_token

if __name__ == "__main__":
    app.run(debug=True)

