"""
This file scrapes Spotify, querying it for all of the songs found in billboard.py
and produces a csv of tempos. The datafile is just numbers because we don't care
what the songs are, we just care about the tempo data.


NOTE: the main for loop of this file isn't written in a function because that adds
an extra level of modularity that isn't necessary. We won't ever be looping and adding
elements to a dataframe except in the context of filling out tempo information in this
file. That's why there's a docstring up here explaining what this entire file does.
"""

from time import sleep
from ast import literal_eval
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml


# import the YAML file as a configuration file so that we can request spotify privately
# DON'T UPLOAD CONFIG.YAML TO GITHUB
with open("../config.yaml", "r", encoding="utf-8") as yaml_file:
    config = yaml.safe_load(yaml_file)


# Define a function that will query spotify and return the tempo of a song
def query_spotify(track, artist):
    """
    Queries Spotify's API for the tempo information corresponding to a track by an artist.

    Args:
        track (str): the track to find bpm info for
        artist (str): the artist of that track

    Returns:
        audio_features["tempo] (int): an integer containing the BPM of that song

        OR

        ValueError: if no song is found corresponding to the query
    """
    search_query = track + ' ' + artist
    search_results = sp.search(q=search_query)
    uri = search_results["tracks"]["items"][0]["uri"]
    audio_features = sp.audio_features(uri)[0]
    return audio_features["Danceability"]


# Define a range of years that you'd like to start and stop querying
START_YEAR = 1940
END_YEAR = 2019

# Open client to begin requesting data
client_credentials_manager = SpotifyClientCredentials(
    client_id=config["SPOTIPY_CLIENT_ID"], client_secret=config["SPOTIPY_CLIENT_SECRET"])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Open the datafile from billboard scraping
song_df = pd.read_csv("../data/top100.csv").set_index("index")

# Initialize an empty dataframe where tempo information will be stored
tempo_df = pd.DataFrame(index=range(
    1, 101), columns=range(START_YEAR, END_YEAR+1))


# Iterate through all of the years of data
for i in range(START_YEAR, END_YEAR+1):
    print("i is now: ", str(i))

    # Iterate through all 100 songs for each year
    for j in range(1, 101):
        print("we are now on the", str(j), "th song")

        # Each cell is a list, but it's saved as a string right now
        # literal_eval will evaluate it as a list
        try:
            next_entry = literal_eval(song_df[str(i)][j])

        # If there is no song in that cell go to next year
        except ValueError:
            break

        # Try to query spotify for BPM info
        try:
            # The track + artist will be the 2nd and 3rd element of the list in the cell
            tempo_df.at[j, i] = query_spotify(next_entry[1], next_entry[2])

        # If song isn't found, set the value as NaN so it doesn't mess with the average
        except (TypeError,IndexError,ValueError) as e:
            print(e)

            tempo_df.at[j, i] = None

    # Pause to avoid over-requesting Spotify
    sleep(1)

# Write the resulting dataframe to a CSV file that visualization.py can use
tempo_df.to_csv("../data/bpm.csv")
tempo_df.to_csv("../data/bpm2.csv")
