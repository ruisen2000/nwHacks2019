import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#username = "ozujzpuiqgx8oo3k0kzj4cnk1"
#scope = 'user-library-read'

client_credentials_manager = SpotifyClientCredentials(client_id='8ec10118123745c98796a0da389e1b35',
                                                      client_secret='832c43bccfe44e6d90cd3ac66cc7e28b')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = spotify.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None