from bs4 import BeautifulSoup
import requests
import spotipy

from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USER_ID

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     scope="playlist-modify-public playlist-modify-private user-library-read"))

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
songs_uri = []
response = requests.get("https://www.billboard.com/charts/hot-100/")

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

for song_name in song_names:
    params = {
    'q': song_name,
    'type': 'track',
    'limit': '1'
    }

    result = sp.search(**params)
    if result['tracks']['items']:
        song = result['tracks']['items'][0]
        song_uri = song['uri']
        songs_uri.append(song_uri)

playlist = sp.user_playlist_create(user=USER_ID, name='Top 100', public=False, description="Top 100 from billboard")

playlist_id = playlist['id']

sp.playlist_add_items(playlist_id=playlist_id, items=songs_uri)

print(f"Playlist created successfully! You can listen to it here: https://open.spotify.com/playlist/{playlist_id}")
