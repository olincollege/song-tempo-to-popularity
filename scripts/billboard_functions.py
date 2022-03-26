import requests
from bs4 import BeautifulSoup
"""
Get data from webpage
"""
def get_data(year):
    url = f"http://billboardtop100of.com/{year}-2/"
    response = requests.get(url)
    data = BeautifulSoup(response.content, 'html.parser')
    return data

"""
Remove all tags and amp

Args:
    tag_type: give < and beginning of tag (e.g. <div or tr)

Returns:
    list: returns the cleaned list without any external links to information
        or images. The external links were originally encased in certain tags.
"""
def remove_long_tags(tag_type, list):
    clean_list = []
    tag_types = ["<div", "<a", "<p", "<td"]
    for i in range(len(list)):
        # if tag_type == "<td":
        #     for j in range(len(list[i])):
        #         list[i][j] = list[i][j].replace("<tr>", "")
        #         list[i][j] = list[i][j].replace("\n", "")
        #         if list[i][j][:3] == "<td":
        #             index = list[i][j].index(">")
        #             list[i][j] = list[i][j][index + 1:]
        if tag_type in tag_types:
            list[i] = str(list[i])
            if tag_type in list[i]:
                index = list[i].index(">")
                list[i] = list[i][index + 1:]
        remove_end_tag = list[i].replace("</" + tag_type[1:] + ">", "")
        remove_unit = remove_end_tag.replace(u"\xa0", u"")
        remove_amp = remove_unit.replace("amp;", "")
        clean_list.append(remove_amp)
    return clean_list

"""
Splits list into groups of three

Args:
    long_list: list of strings that is divisible by three. Contains rank,
        artist, and song for all 100 top songs of each year. This list is
        300 elements long.

"""
def split_list_into_three(long_list):
    split_list = [long_list[i:i+3] for i in range(0, len(long_list), 3)]
    return split_list

"""
Loads the data from a specific year into the data frame

"""
def import_to_df(split_list, year, df):
    for i in range(1, len(split_list) + 1):
        df.at[i, year] = split_list[i - 1]
        
    df.to_csv("../data/top100.csv")