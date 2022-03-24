"""
Scraping Billboard Top 100's most popular songs from 1950 - Present day

Produce a csv containing a 72x100 table (each row is a year, each column is a ranking)
"""
# need to get year, rank, track, artist

from numpy import char
import requests
import json
from bs4 import BeautifulSoup
# 1963
url = "http://billboardtop100of.com/1963-2/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
s = soup.findAll('tr')

print(s)

for item in s:
    remove_td = item.replace("<td>", "")
    remove_td = remove_td.replace("</td>", "")
# 2018
# url = "http://billboardtop100of.com/2018-2/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# s = soup.findAll(True, {'class':["ye-chart-item__rank", "ye-chart-item__title", "ye-chart-item__artist"]})

# no_div_list = []
# for item in s:
#     item = str(item)
#     i = 0
#     div_tag = ""
#     if item[:2] == "<d":
#         while item[i] != ">":
#             div_tag += item[i]
#             i += 1
#         div_tag += ">"
#         item = item.replace(div_tag, "")
#     item = item.replace("amp;", "")
#     item = item.replace("</div>", "")
#     i = 0
#     a_tag = ""
#     if item[:2] == "<a":
#         while item[i] != ">":
#             a_tag += item[i]
#             i += 1
#         a_tag += ">"
#     item = item.replace(a_tag, "")
#     item = item.replace("</a>", "")
#     no_div_list.append(item)
# print(no_div_list)

# no_div_list = [no_div_list[i:i+3] for i in range(0, len(no_div_list), 3)]
# artist_dict = {}
# # for Richard -- this doesn't include rank
# for element in no_div_list:
#     artist_dict[element[2]] = element[1]     # key = artist, value = song

# print ("{:<50} {:<50}".format('ARTIST', 'SONG'))
 
# # print each data item.
# for artist, song in artist_dict.items():
#     # artist, song = song
#     print ("{:<50} {:<50}".format(artist, song))

# only works for 2019!!!!
# url = "http://billboardtop100of.com/2019-2/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# s = soup.find_all('p')
# s = s[:298]     # remove extra unnecessary stuff

# # loop through url to http.get from a new page
# clean_list = []
# all_a_tags = []

# # list for all line breaks split up (removing <br/> and splitting there)
# split_list = []
# for item in s:
#     item = str(item)
#     if "<br/>" in item:
#         split_br = item.split("<br/>")
#         split_list += split_br
#     else:
#         split_list.append(item)

# # remove all amps, p tags, and \xa0
# for i in range(len(split_list)):
#     remove_amp = str(split_list[i]).replace("amp;", "")
#     remove_p_tag = str(remove_amp).replace("<p>", "")
#     remove_second_p_tag = str(remove_p_tag).replace("</p>", "")
#     clean = str(remove_second_p_tag).replace(u"\xa0", u"")
#     clean_list.append(clean)

# # remove all sites from elements
# final_list = [] 

# for item in clean_list:
#     i = 0
#     a_tag = ""
#     if item[:2] == "<a":
#         while item[i] != ">":
#             a_tag += item[i]
#             i += 1
#         a_tag += ">"
#     item = item.replace(a_tag, "")
#     item = item.replace("</a>", "")
#     final_list.append(item)

# print(final_list)
# # Split everything into groups of three
# split_list = [final_list[i:i+3] for i in range(0, len(final_list), 3)]

# artist_dict = {}
# # for Richard -- this doesn't include rank
# for element in split_list:
#     artist_dict[element[2]] = element[1]     # key = artist, value = song

# print ("{:<50} {:<50}".format('ARTIST', 'SONG'))
 
# # print each data item.
# for artist, song in artist_dict.items():
#     # artist, song = song
#     print ("{:<50} {:<50}".format(artist, song))