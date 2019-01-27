import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

username = "ozujzpuiqgx8oo3k0kzj4cnk1"
token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id='8ec10118123745c98796a0da389e1b35', client_secret='832c43bccfe44e6d90cd3ac66cc7e28b', redirect_uri='https://localhost:8080')

if token:
    sp = spotipy.Spotify(auth=token)
    print("Hello")

