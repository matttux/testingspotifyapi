import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '30eddc6c80874352b506e59332b12186
'
client_secret = '59d7cf725ffb4b28b4b8d41398c78412'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
