from zenora import APIClient
from flask import Flask, render_template, request, session, redirect
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
client = APIClient(TOKEN, client_secret=CLIENT_SECRET)

@app.route("/")
def home():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template('index.html', current_user=current_user)
    return render_template("index.html", oauth_url=OAUTH_URL)

@app.route("/oauth/callback")
def callback():
    code = request.args['code']
    access_token = client.oauth.get_access_token(code=code, redirect_uri=REDIRECT_URI).access_token
    session['token'] = access_token
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
