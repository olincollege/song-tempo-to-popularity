"""
Test that the functions in billboard_functions.py are working properly.

There is no function test for creating the final list of lists of music data
for years 1940, 1942-1944, 2013, and 2015-2020. This is because these years
contained more messy and complexly parsed data that needed a little more
cleaning than the years that could simply use the complete_billboard
function to generate the final list of lists of cleaned music data.
"""

import pytest
from billboard_functions import (
    clean_data,
    split_and_extend,
    split_list_into_three,
)

# Check that the split_list_into_three function splits a list of strings into
# a list of lists for every three elements in the original list.
CLEAN_DATA_CASES = [
    # Case where the start tag is in the middle of the string.
    (("<a",["abcd<a89%justinbieber>dcba</a>"]), ["dcba"]),
    # Case with no start tag but has an end tag.
    (("<p", ["theweeknd</p>usher"]),["theweekndusher"]),
    # Case where everything is encased in a start tag.
    (("<div", ["<divtheweeknd>"]), [""]),
    # A tag type that is not in the tag_types list.
    (("<h6", ["abc<li theweeknd>"]), ["abc<li theweeknd>"]),
    # Case with extra info (\n, amp;, \xa0)
    (("<td", ["abc/n<td the weeknd>", "justin bieber \xa0&amp; nicki minaj\n"]),
    ["", "justin bieber & nicki minaj"]),
]

# Couldn't figure out how to test bs4 BeautifulSoup elemeents.
SPLIT_EXTEND_CASES = [
    # Case with multiple br end tags.
    ((1945, ["1. All Me Whitney<br/>2. Umbrella Rihanna<br/>3. Baby Justin"], "<br/>"),
    ["1. All Me Whitney", "2. Umbrella Rihanna", "3. Baby Justin"]),
    # Case with no br end tags and a year that isn't actually searched for.
    ((2020, ["1. All Me Whitney 2. Umbrella Rihanna"], "<br/>"),
    ["1. All Me Whitney 2. Umbrella Rihanna"]),
    # Case with br tag in the beginning.
    ((2019, ["<br/>1. All Me Whitney<br/>2. Umbrella Rihanna"], "<br/>"),
    ["", "1. All Me Whitney", "2. Umbrella Rihanna"]),
    # Check case with different tag.
    ((2015, ["1. All Me - Whitney 2. Umbrella - Rihanna"], ". "),
    ["1", "All Me - Whitney 2", "Umbrella - Rihanna"]),
    # Check one of the years in special_years.
    ((1942, ["All Me - Whitney", "Umbrella - Rihanna"], " - "),
    ["All Me", "Whitney"])
]

SPLIT_LIST_CASES = [
    # A list of length divisible by three.
    (['2', 'Sunflower','Post Malone & Swae Lee', '2', 'Circles', 'Post Malone'],
    [['2', 'Sunflower', 'Post Malone & Swae Lee'],
    ['2', 'Circles', 'Post Malone']]),
    # A list of length not divisible by three.
    (['2', 'Sunflower','Post Malone & Swae Lee', '2', 'Circles'],
    [['2', 'Sunflower', 'Post Malone & Swae Lee'], ['2', 'Circles']]),
    # An empty list.
    ([], []),
    # A list of length less than three.
    (['2', 'Sunflower'], [['2', 'Sunflower']])
]

@pytest.mark.parametrize("source_text, split_text", SPLIT_LIST_CASES)
def test_split_list_into_three(source_text, split_text):
    """
    Check that remove_tags() removes the information within beginning and
    end tags.

    Args:
        source_text: A list of strings representing the source text.
        split_text: A list of lists representing the strings in source_text
            grouped by three.
    """
    assert split_list_into_three(source_text) == split_text

@pytest.mark.parametrize("source_text, result_list", SPLIT_EXTEND_CASES)
def test_split_and_extend(source_text, result_list):
    # HOW TO KNOW WHAT CHARACTER STRING IT'S LOOKING FOR?
    """
    Check that split_and extend() splits string in all instances of a given
    character string and extends the result onto a list to avoid creating a
    list of lists.

    Args:
        source_text: A list of a string representing the source text.
        split_list: A list of strings representing the string in source_text
            split at instances of the given char string.
    """
    year = source_text[0]
    split_list = source_text[1]
    char = source_text[2]
    assert split_and_extend(year, split_list, char) == result_list

@pytest.mark.parametrize("source_text, clean_text", CLEAN_DATA_CASES)
def test_clean_data(source_text, clean_text):
    """
    Check that remove_tags() removes the information within beginning and
    end tags.

    Args:
        source_text: A list of strings representing the source text.
        split_text: A list of strings representing the source text without
            tags and extraneous characters or information.
    """
    tag_type = source_text[0]
    long_list = source_text[1]
    assert clean_data(tag_type, long_list) == clean_text
