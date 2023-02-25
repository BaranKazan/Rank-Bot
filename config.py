import os
from urllib import parse

TOKEN = os.getenv("TOKEN")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GUILD_ID = 622450248362754050
REDIRECT_URI = "http://127.0.0.1:5000/oauth/callback"
OAUTH_URL= f"https://discord.com/api/oauth2/authorize?client_id=1065658317487210496&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify%20guilds"
