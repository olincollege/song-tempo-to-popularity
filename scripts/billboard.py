"""
Scraping Billboard Top 100's most popular songs from 1950 - Present day

Produce a csv containing a 72x100 table (each row is a year, each column is a ranking)
"""
from billboard_functions import *
from os import remove
from stat import SF_APPEND
import pandas as pd
import requests
from bs4 import BeautifulSoup

# create data frame
df = pd.DataFrame(index = range(1,101), columns = range(1940,2021))
# 1945 - 2014 are all <div> tags for the body
year = 1945
# loop through 1945 to 2014 (all tr tags)
while year <= 2014:
    data = get_data(year)
    music_data = data.findAll("td")
    clean_data = remove_long_tags("<td", music_data)
    split_list = split_list_into_three(clean_data)
    import_to_df(split_list, year, df)

    year += 1
# 1963
# soup = get_data(1963)
# s = soup.findAll('tr')
# s = s[:2]

# split_list = []
# for element in s:
#     element = str(element)
#     split_element = element.split("</td>")
#     split_list.extend(split_element[:-1])
# clean_list = remove_long_tags("<td", split_list)

# 2018
# url = "http://billboardtop100of.com/2018-2/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# s = soup.findAll(True, {'class':["ye-chart-item__rank", "ye-chart-item__title", "ye-chart-item__artist"]})

# clean_soup = remove_long_tags("<div", s)
# cleaner_soup = remove_long_tags("<a", clean_soup)

# # only works for 2019!!!!
# data = get_data(2019)
# # print(soup)
# music_data = data.find_all('p')
# music_data = music_data[:298]     # remove extra unnecessary stuff

# # list for all line breaks split up (removing <br/> and splitting there)
# split_list = []
# for item in music_data:
#     item = str(item)
#     if "<br/>" in item:
#         split_br = item.split("<br/>")
#         split_list += split_br
#     else:
#         split_list.append(item)

# # remove all amps, p tags, and \xa0
# clean_list = remove_long_tags("<p", split_list)
# final_list = remove_long_tags("<a", clean_list)
# print(final_list)