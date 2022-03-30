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
from billboard_functions import *
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Create the data frame
df = pd.DataFrame(index = range(1,101), columns = range(1940,2021))

# 1940
data = get_data(1940)
music_data = data.find_all("p")

# split list at br end tag
split_list = []
for element in music_data[:-1]:
    element = str(element)
    split_br = element.split("<br/>")
    split_list.extend(split_br)

remove_n_p = remove_long_tags("<p", split_list)

split_rank_list = []
for item in remove_n_p:
    item = item.replace("Opus No. 1", "Opus No.1")
    item = item.replace("G.I. Jive", "G.I.Jive")
    split_rank = item.split(". ")
    split_rank_list.extend(split_rank)

split_list = []
for item in split_rank_list:
    split_song_info = item.split(" – ")
    split_list.extend(split_song_info)

final_list = split_list_into_three(split_list)
import_to_df(final_list, 1940, df)

# 1941
split_list = complete_billboard(1941, "td")
import_to_df(split_list, 1941, df)


# 1942
data = get_data(1942)
music_data = data.findAll("p")

# split list at br end tag
split_list = []
for element in music_data[:-1]:
    element = str(element)
    split_br = element.split("<br/>")
    split_list.extend(split_br)

    # remove extraneous info
    for item in split_list:
        if "vocals by" in item:
            split_list.remove(item)
        if "vocal by" in item:
            split_list.remove(item)
        if "written by" in item:
            split_list.remove(item)

# just remove p tags
filler_list = remove_long_tags("<p", split_list)

split_by_rank_list = []
split_by_by_list = []
clean_list = []

# split by ". " (e.g. "9. Blues in the Night" --> ["9.", "Blues in the Night"])
for item in filler_list:
    split_rank = item.split(". ")
    split_by_rank_list.extend(split_rank)

# split by "by"
for item in split_by_rank_list:
    split_song = item.split(" by ")
    split_by_by_list.extend(split_song)

for item in split_by_by_list:
    split_rank = item.split(".")
    clean_list.extend(split_rank)
# remove excess info
clean_list.remove(clean_list[189])
clean_list.remove(clean_list[190])

final_list = split_list_into_three(clean_list)
import_to_df(final_list, 1942, df)

# # 1943, 1944
year = 1943
while year <= 1944:
    data = get_data(1943)
    music_data = data.find_all("p")

    # split list at br end tag
    split_list = []
    for element in music_data[:-1]:
        element = str(element)
        split_br = element.split("<br/>")
        split_list.extend(split_br)
    remove_n_p = remove_long_tags("<p", split_list)

    split_list = []
    for item in remove_n_p:
        split_song_info = item.split(" – ")
        split_list.extend(split_song_info)

    clean_list = []

    for item in split_list:
        split_rank = item.split(". ")
        clean_list.extend(split_rank)

    final_list = split_list_into_three(clean_list)
    import_to_df(final_list, year, df)

    year += 1

# 1945 - 2016 contain td tags for the body
        # not 2013
year = 1945
# loop through 1945 to 2016 (all tr tags)
while year <= 2016:
    split_list = complete_billboard(year, "td")
    import_to_df(split_list, year, df)

    year += 1

    # 2013 has different tags, so skip that one
    if year == 2013:
        year += 1

# 2013
data = get_data(2013)
music_data = data.find_all("p")
print(music_data)

# split list at br end tag
split_list = []
for element in music_data[:-1]:
    element = str(element)
    split_br = element.split("<br/>")
    split_list.extend(split_br)
remove_n_p = remove_long_tags("<p", split_list)

split_list = []
for item in remove_n_p:
    split_song_info = item.split(" – ")
    split_list.extend(split_song_info)

clean_list = []

for item in split_list:
    split_rank = item.split(". ")
    clean_list.extend(split_rank)

final_list = split_list_into_three(clean_list)
import_to_df(final_list, 2013, df)

# 2015
data = get_data(2015)
music_data = data.findAll("h6")
clean_data = remove_long_tags("<h6", music_data)
clean_data.remove(clean_data[78])
split_list = split_list_into_three(clean_data)
import_to_df(split_list, 2015, df)

# 2016 
data = get_data(2016)
music_data = data.findAll("td")
remove_td = remove_long_tags("<td", music_data)

clean_list = []
for element in remove_td:
    remove_strong = element.replace("<strong>", "")
    remove_strong_end = remove_strong.replace("</strong>", "")
    remove_p = remove_strong_end.replace("<p>", "")
    remove_p_end = remove_p.replace("</p>", "")
    clean_list.append(remove_p_end)
# remove a-tag. cant' use function bc song is BEFORE start of tag
for i in range(len(clean_list)):
        if "<" in clean_list[i]:
            index = clean_list[i].index("<")
            clean_list[i] = clean_list[i][:index]

split_list = split_list_into_three(clean_list)
import_to_df(split_list, 2016, df)

# 2017&2018
year = 2017
while year <= 2018:
    data = get_data(2017)
    music_data = data.findAll(True, {'class':["ye-chart-item__rank", "ye-chart-item__title", "ye-chart-item__artist"]})
    clean_data = remove_long_tags("<div", music_data)
    clean_data_2 = remove_long_tags("<a", clean_data)
    import_to_df(final_list, year, df)

    year += 1

# only works for 2019!!!!
data = get_data(2019)
music_data = data.find_all('p')
music_data = music_data[:298]     # remove extra unnecessary stuff

# list for all line breaks split up (removing <br/> and splitting there)
split_list = []
for item in music_data:
    item = str(item)
    if "<br/>" in item:
        split_br = item.split("<br/>")
        split_list += split_br
    else:
        split_list.append(item)

# remove all amps, p tags, and \xa0
clean_list = remove_long_tags("<p", split_list)
final_list = remove_long_tags("<a", clean_list)
final_list = split_list_into_three(final_list)
import_to_df(final_list, 2019, df)


# 2020
url = "http://billboardtop100of.com/billboard-top-100-songs-2020-2/"
response = requests.get(url)
data = BeautifulSoup(response.content, "html.parser")
music_data = data.findAll("p")
music_data = music_data[:-2]

split_by_strong_list = []
clean_list = []
cleaner_list = []
for i in range(len(music_data)):
    music_data[i] = str(music_data[i])
    remove_p = music_data[i].replace("<p>", "")
    remove_unit = remove_p.replace(u"\xa0", u"")
    remove_p_end = remove_unit.replace("</p>", "")
    remove_strong = remove_p_end.replace("<strong>", "")
    split_by_strong = remove_strong.split("</strong>")
    split_by_strong_list.extend(split_by_strong)
clean_list = remove_long_tags("<a", split_by_strong_list)

# remove empty elements
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

import_to_df(split_list, 2020, df)