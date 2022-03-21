""" 
Scraping Spotify for all of the songs found in billboard.py

Produces a csv matching individual songs to popularity and BPM

NOTE: We don't care what the songs are, we just care about the popularity v.s. BPM
"""

import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml

with open ("../config.yaml","r") as yaml_file:
    config = yaml.safe_load(yaml_file)



# Authentication - without user


# print(config["SPOTIPY_CLIENT_SECRET"])

client_credentials_manager = SpotifyClientCredentials(client_id=config["SPOTIPY_CLIENT_ID"], client_secret=config["SPOTIPY_CLIENT_SECRET"])
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# grabs a playlist
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
playlist_items = sp.playlist_tracks(playlist_URI)["items"]
playlist = playlist_items[2]["track"]["name"]


track_link = ""
track_URI = track_link.split("/")[-1].split("?")[0]

# print(playlist)
# track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

track = "Favorite Boy"
artist = "Aeio"
searchQuery = track + ' ' + artist 
searchResults = sp.search(q=searchQuery)

print(type(searchResults))
# print(type(searchResults))

uri = searchResults["tracks"]["items"][0]["uri"]
print(uri)
# view the results of the search
# print(json.dumps(searchResults,indent = 4))

audio_features = sp.audio_features(uri)
print(audio_features[0]["tempo"])

"""
for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name = track["track"]["name"]
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]
    
    #Album
    album = track["track"]["album"]["name"]
    # print(track_name)
    
    #Popularity of the track
    track_pop = track["track"]["popularity"]
    
    sp.audio_features(track_uri)[0]
"""