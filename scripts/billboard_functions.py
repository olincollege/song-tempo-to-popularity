import requests
from bs4 import BeautifulSoup

"""
Gets all information from a given url and parses it using Beautiful Soup.

Args:
    year: An integer representing the year that is being searched for in
        Billboard Top 100. 
        
        This web scraping code only scrapes from years 1940 to 2020. 1940 is
        the earliest year that the Billboard Top 100 holds data for. The
        Billboard Top 100 for 2021 was not scraped, since the formatting
        was too complex to clean given the timeframe.

Returns: A list of class bs4.BeautifulSoup data types. This represents all
    information scraped and parsed by Beautiful Soup for the given year.
"""
def get_data(year):
    # Years 1940 and 2020 had different URLs than every other year 
    if year == (2020):
        url = "http://billboardtop100of.com/billboard-top-100-songs-2020-2/"
    elif year == 1940:
        url = "http://billboardtop100of.com/336-2/"
    else:
        url = f"http://billboardtop100of.com/{year}-2/"
    response = requests.get(url)
    data = BeautifulSoup(response.content, "html.parser")
    return data

"""
Significantly cleans up the data for a certain tag type. This function will
replace all instances of the tag type passed in with an empty string. By doing
so, it also removes any external links to additional information or album
covers.

This function cleans up the data even more by replacing any instances of unit
code, "amp;", and new lines ("\n"). For the data of 1940, 1943, and 1944, this
function also replaces any forward slashes with commas.

    i.e. "Kay Kyser / Gene Autry" --> "Kay Kyser, Gene Autry

Args:
    tag_type: A string consisting of "<" and the tag type (e.g. <div or <td).

        This function allows any tag_type as a parameter, but will only clean
        the data for the tag types present in the list tag_types: div, a, p, td,
        strong, and h6.

Returns:
    clean_list: returns the cleaned list without any instances of the given
        tags, external links to information or images, or anything else
        explained in the function's description. 
        
        The external links were originally encased in certain tags.
"""
def remove_long_tags(tag_type, list):
    clean_list = []
    tag_types = ["<div", "<a", "<p", "<td", "<strong", "<h6"]

    for i in range(len(list)):
        if tag_type in tag_types:
            list[i] = str(list[i])
            if tag_type in list[i]:
                index = list[i].index(">")
                list[i] = list[i][index + 1:]
        remove_end_tag = list[i].replace("</" + tag_type[1:] + ">", "")

        # Remove any other unnecessary data
        remove_unit = remove_end_tag.replace(u"\xa0", u"")
        remove_amp = remove_unit.replace("amp;", "")
        remove_n = remove_amp.replace("\n", "")

        # Only necessary for 1940, 1943, 1944
        remove_backslash = remove_n.replace(" /", ",")
        clean_list.append(remove_backslash)
    return clean_list
"""
Splits a given list into a list of lists by grouping the elements of the
original list into groups of three. If the length of the list is not evenly
divisible by three, this list comprehension will simply group the left over one
or two elements into a list like all of the others.

    i.e. ["1", "Ke$ha", "TiK ToK", "2", "Lady Antebellum"] -->
         [["1", "Ke$ha", "TiK ToK"], ["2", "Lady Antebellum"]]

This is the format required (for our version of this project) to load onto the
dataframe in an easily readable manner. All correlating information is grouped
together.

Args:
    long_list: A list of strings. Contains rank, artist, and song for all 100
        top songs of the respective year. If the cleaning of the data has been
        done successfully, this list will be 300 elements long.

Returns:
    split_list: A list of lists, which are made up of strings. Each element in
        split_list contains the song's rank, artist, and song as separate
        elements in that order.
"""
def split_list_into_three(long_list):
    split_list = [long_list[i:i+3] for i in range(0, len(long_list), 3)]
    return split_list

"""
Loads the data from a specific year into the data frame.

Args:
    split_list: A list of lists, which are made up of strings. Each element in
        split_list contains the song's rank, artist, and song as separate
        elements in that order.

    year: An integer representing the year that the data concerns.

    df: A data frame that contains 80 columns (one for every year searched for)
        and 100 rows (one for every song on the Billboard Top 100 for each
        year).

Returns:
    This function does not return anything, but instead loads the data into
    the data frame in the file top100.csv.
"""
def import_to_df(split_list, year, df):
    for i in range(1, len(split_list) + 1):
        df.at[i, year] = split_list[i - 1]
        
    df.to_csv("../data/top100.csv")

"""
Completes the entire process of scraping, cleaning, and separating the data
into a list of lists. This function does not import the data to the dataframe.

This function only works for years 1941 and 1945-2016 (skipping 2013, 2015,
2016). This function was not called for all other years, since those were of
more messy (complexly parsed, or not clean) data and could not be easily cleaned
using this function.

Args:
    year: An integer representing the year that the data concerns.

    tag: A string representing the HTML tag to look for and clean in the data.

        i.e. "div", "td", "h6"

Returns:
    split_list: A list of lists, which are made up of strings. Each element in
            split_list contains the song's rank, artist, and song as separate
            elements in that order. This can be then cleanly loaded into the
            dataframe.
"""
def complete_billboard(year, tag):
    data = get_data(year)
    music_data = data.findAll(tag)
    clean_data = remove_long_tags("<" + tag, music_data)

    # Just in case there are any external links to images, etc.
    clean_data_more = remove_long_tags("<a", clean_data)
    split_list = split_list_into_three(clean_data_more)
    return split_list
