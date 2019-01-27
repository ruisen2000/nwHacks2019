import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

username = "ozujzpuiqgx8oo3k0kzj4cnk1"
token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id='8ec10118123745c98796a0da389e1b35', client_secret='832c43bccfe44e6d90cd3ac66cc7e28b', redirect_uri='https://localhost:8080')

selected_playlist = 'ff'
track_id = list()
track_duration = list() # in ms
new_tracks = list()
user_playlistDict = {}

productive = ['37i9dQZF1DX1OY2Lp0bIPp', '37i9dQZF1DWUvQoIOFMFUT']
workout = ['37i9dQZF1DX76Wlfdnj7AP', '37i9dQZF1DXdxcBWuJkbcy']
sleep = ['37i9dQZF1DWUXaCLIrt6jX', '37i9dQZF1DX3Ogo9pFvBkY']
nostalgic = ['37i9dQZF1DWWwaxRea1LWS', '37i9dQZF1DXbTxeAdrVG2l']

max_time = 1786140
sum = 0

if token:
    sp = spotipy.Spotify(auth=token)
    
    # track to get stuff from
    track1 = sp.user_playlist_tracks("spotify", playlist_id="37i9dQZF1DX6ziVCJnEm59")
    
    # Get my playlists.  
    my_playlists = sp.user_playlists(username)
    for i, my_playlists in enumerate(my_playlists['items']):
        user_playlistDict[my_playlists['name']] = my_playlists['id']
    
    # If selected playlist doesnt exist, create it and add it to dict
    if user_playlistDict.get(selected_playlist) == None:
        print(user_playlistDict)
        ret = sp.user_playlist_create(username, selected_playlist, public=True)
        if ret.get('id') is not None:
            user_playlistDict[ret['name']] = ret['id']
            
        my_playlists = sp.user_playlists(username)
    
    playlist_id = user_playlistDict[selected_playlist]
    
    # save all tracks from the appropriate playlist
    for item in track1['items']:
        track_id.append(item['track']['uri'])
        track_duration.append(item['track']['duration_ms'])
       
    # select tracks that fill up the max time set from user
    for i in range(1,len(track_id)):
        if sum + track_duration[i] < max_time:
            sum = sum + track_duration[i]
            new_tracks.append(track_id[i])
            sp.user_playlist_replace_tracks(username, playlist_id, new_tracks)

    
   # print(playlists)