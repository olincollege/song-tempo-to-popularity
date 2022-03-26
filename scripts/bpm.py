""" 
Scraping Spotify for all of the songs found in billboard.py

Produces a csv matching individual songs to popularity and BPM

NOTE: We don't care what the songs are, we just care about the popularity v.s. BPM
"""

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml
from ast import literal_eval

with open ("../config.yaml","r") as yaml_file:
    config = yaml.safe_load(yaml_file)

def query_spotify(track,artist):
    searchQuery = track + ' ' + artist 
    searchResults = sp.search(q=searchQuery)
    uri = searchResults["tracks"]["items"][0]["uri"]
    audio_features = sp.audio_features(uri)[0]
    return audio_features["tempo"]


# Authentication - without user


# print(config["SPOTIPY_CLIENT_SECRET"])

client_credentials_manager = SpotifyClientCredentials(client_id=config["SPOTIPY_CLIENT_ID"], client_secret=config["SPOTIPY_CLIENT_SECRET"])
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

track = "Favorite Boy"
artist = "Aeio"


# print(query_spotify(track,artist))

# data = {''}
song_df = pd.read_csv("../data/top100.csv").set_index("index")

tempo_df = pd.DataFrame(index = range(1,101), columns = range(1940,2022))

# next = literal_eval(df["2018"][0])



for i in range(1,101):
    next_entry = literal_eval(song_df["2018"][i])
    track = next_entry[1]
    artist = next_entry[2]
    try: 
        tempo_df.at[i,2018] = query_spotify(track,artist)
    except IndexError:
        tempo_df.at[i,2018] = None
print(tempo_df)
tempo_df.to_csv("../data/bpm.csv")


# df.at[1,1940] = query_spotify(track,artist)
# print(df)

# with open ("../data/bpm.csv","a") as f:
#     dictwriter = csv.DictWriter(f, fieldnames = headers)
#     new_entry = query_spotify(track,artist)
#     print(type(new_entry["tempo"]))

# print(audio_features[0]["energy"])
