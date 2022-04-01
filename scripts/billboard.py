"""
Scraping Billboard Top 100's most popular songs from 1940 - 2020. This code
does the actual scraping, cleaning, and loading of the data onto the data frame,
or calls functions from billboard_functions.py to do so.

It's important to note that the data from some of the years could not be cleaned
purely by calling the complete_billboard function from billboard_functions.py,
since the parsed HTML code was a little more messy. There were too many unique
cases to justify making a more complex complete_billboard or remove_long_tags
function.

This file is meant to create a list of lists for each year containing the
rank, artist, and song for each top song of the year. It then produces a csv
containing a 80x100 table (column = year, row = song) that will then be run
through the Spotipy API wrapper to find the tempo (BPM) of each song.
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
from billboard_functions import complete_billboard, get_data, clean_data, \
import_to_df, split_and_extend, split_list_into_three
# Create the data frame
dataframe = pd.DataFrame(index=range(1, 101), columns=range(1940, 2021))


# SCRAPE & CLEAN 1940 DATA
data = get_data(1940)
music_data = data.find_all("p")

# split data list at "<br/>"" into elements that contain song information
split_list = split_and_extend(1940, music_data, "</br>")

# Remove p tags and any other unnecessary characters
remove_n_p = clean_data("<p", split_list)

# Fix any specific formatting issues and split into elements between rank
# and song
split_rank_list = []
for item in remove_n_p:
    item = item.replace("Opus No. 1", "Opus No.1")
    item = item.replace("G.I. Jive", "G.I.Jive")
    split_rank = item.split(". ")
    split_rank_list.extend(split_rank)

# Create the cleaned list of strings by splitting into elements between song
# and artist
split_list = split_and_extend(1940, split_rank_list, " – ")

# # Group the elements in the list by three to easily load onto the data frame
final_list = split_list_into_three(split_list)
import_to_df(final_list, 1940, dataframe)


# SCRAPE & CLEAN 1941 DATA
split_list = complete_billboard(1941, "td")
import_to_df(split_list, 1941, dataframe)

# SCRAPE & CLEAN 1942 DATA
data = get_data(1942)
music_data = data.findAll("p")

# split data list at "<br/>"" into elements that contain song information
split_list = split_and_extend(1942, music_data, "</br>")

remove_p = clean_data("<p", split_list)
remove_p[85] = "Mr. Five by Five"

# Remove extraneous information
removal_list = []
for item in remove_p:
    if "vocals by" in item:
        removal_list.append(item)
    if "vocal by" in item:
        removal_list.append(item)
    if "written by" in item:
        removal_list.append(item)

for item in removal_list:
    remove_p.remove(item)

# Clean up by removing p-tags and other unnecessary characters
filler_list = clean_data("<p", remove_p)

split_by_rank_list = []
split_by_by_list = []
clean_list = []

# Split by ". " (e.g. "9. Blues in the Night" --> ["9.", "Blues in the Night"])
split_by_rank_list = split_and_extend(1942, filler_list, ". ")

# Split song and artist by " by "
split_by_by_list = split_and_extend(1942, split_by_rank_list, " by ")

# Split by any of the wrongly-formatted songs
clean_list = split_and_extend(1942, split_by_by_list, ".")

# Remove excess information
clean_list.remove(clean_list[62])
clean_list.remove(clean_list[10])
clean_list.remove(clean_list[11])
clean_list.remove(clean_list[12])
clean_list.remove(clean_list[189])
clean_list.remove(clean_list[190])

final_list = split_list_into_three(clean_list)
import_to_df(final_list, 1942, dataframe)

# 1943, 1944
for year in range(1943, 1945):
    data = get_data(year)
    music_data = data.find_all("p")

    # split list at br end tag
    split_list = split_and_extend(year, music_data, "<br/>")
    remove_n_p = clean_data("<p", split_list)

    split_song_artist = split_and_extend(year, remove_n_p, " – ")

    clean_list = split_and_extend(year, split_rank, ". ")

    final_list = split_list_into_three(clean_list)
    import_to_df(final_list, year, dataframe)

# loop through 1945 to 2014 (all tr tags)
for year in range(1945, 2015):
    split_list = complete_billboard(year, "td")
    import_to_df(split_list, year, dataframe)

    # 2013 has different tags, so skip that one
    if year == 2013:
        continue

# 2013
data = get_data(2013)
music_data = data.find_all("p")

# Split list at br end tag
split_list = split_and_extend(2013, music_data, "</br>")

# Separate and clean data
remove_n_p = clean_data("<p", split_list)
split_list = split_and_extend(2013, remove_n_p, " – ")
clean_list = split_and_extend(2013, split_list, ". ")

# Split into final list of lists to import
final_list = split_list_into_three(clean_list)
import_to_df(final_list, 2013, dataframe)

# 2015
data = get_data(2015)
music_data = data.findAll("h6")

# Clean data
clean_list = clean_data("<h6", music_data)
clean_list.remove(clean_list[78])

# Split into final list of lists to import
split_list = split_list_into_three(clean_data)
import_to_df(split_list, 2015, dataframe)

# 2016
data = get_data(2016)
music_data = data.findAll("td")
remove_td = clean_data("<td", music_data)

# Clean data -- couldn't use clean_data()
clean_list = []
for element in remove_td:
    remove_strong = element.replace("<strong>", "")
    remove_strong_end = remove_strong.replace("</strong>", "")
    remove_p = remove_strong_end.replace("<p>", "")
    remove_p_end = remove_p.replace("</p>", "")
    clean_list.append(remove_p_end)

# Remove a-tag. Can't use clean_data() because song is BEFORE start of tag
for i, _ in enumerate(clean_list):
    clean_list[i] = str(clean_list[i])
    if "<" in clean_list[i]:
        index = clean_list[i].index("<")
        clean_list[i] = clean_list[i][:index]

# Split into final list of lists to import
split_list = split_list_into_three(clean_list)
import_to_df(split_list, 2016, dataframe)

# 2017&2018
for year in range(2017, 2019):
    data = get_data(year)
    music_data = data.findAll(True, {'class': [
                              "ye-chart-item__rank", "ye-chart-item__title",
                              "ye-chart-item__artist"]})

    # Clean data
    remove_div = clean_data("<div", music_data)
    clean_list = clean_data("<a", remove_div)
    split_list_into_three(clean_list)
    import_to_df(final_list, year, dataframe)


# 2019
data = get_data(2019)
music_data = data.find_all('p')
music_data = music_data[:298]     # remove extra unnecessary stuff

# List for all line breaks split up (removing <br/> and splitting there)
split_list = []

for i, _ in enumerate(music_data):
    music_data[i] = str(music_data[i])
    if "<br/>" in music_data[i]:
        split_br = music_data[i].split("<br/>")
        split_list += split_br
    else:
        split_list.append(music_data[i])

# Remove all amps, p tags, and \xa0
clean_list = clean_data("<p", split_list)
final_list = clean_data("<a", clean_list)
final_list = split_list_into_three(final_list)
import_to_df(final_list, 2019, dataframe)


# 2020
URL = "http://billboardtop100of.com/billboard-top-100-songs-2020-2/"
response = requests.get(URL)
data = BeautifulSoup(response.content, "html.parser")
music_data = data.findAll("p")
music_data = music_data[:-2]

split_by_strong_list = []
clean_list = []
cleaner_list = []

remove_p = clean_data("<p", music_data)

for i, _ in enumerate(music_data):
    # music_data[i] = str(music_data[i])
    remove_p = clean_data("<p", music_data)
    remove_p = music_data[i].replace("<p>", "")
    remove_unit = remove_p.replace(u"\xa0", u"")
    remove_p_end = remove_unit.replace("</p>", "")
    remove_strong = remove_p_end.replace("<strong>", "")
    split_by_strong = remove_strong.split("</strong>")
    split_by_strong_list.extend(split_by_strong)
clean_list = clean_data("<a", split_by_strong_list)

# Remove all empty elements of clean_list
filler_list = []
filler_list = list(filter(None, clean_list))
filler_list.remove(filler_list[9])

final_list = []
# Still have to fix one thing wrong...
for element in filler_list:
    if "92" in element:
        split_92 = element.split("2 ")
        split_92[0] = split_92[0] + "2"
        final_list.extend(split_92)
    else:
        final_list.append(element)
split_list = split_list_into_three(final_list)

import_to_df(split_list, 2020, dataframe)
