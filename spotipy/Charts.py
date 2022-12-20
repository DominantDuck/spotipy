import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import libraries
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="6765523b6eb6425e907d1ab7c24c9906",
                                                           client_secret="-"))


# get track ids from playlist
def getPlaylistTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getPlaylistTrackIDs('100keepit', '5w99BzxT7OOCz2oEkKCReG')  # Drake Complete


# get song info and audio analysis from song ids
def getTrackFeatures(id):
    meta = sp.track(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    track = [name, album, artist, release_date, length, popularity]
    return track

    tracks = []
    for i in range(0, 5):
        time.sleep(.5)
        track = getTrackFeatures(ids[i])
        tracks.append(track)

    df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity'])
    print(df)
