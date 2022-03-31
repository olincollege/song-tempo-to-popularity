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
    split_by_br,
    split_and_extend,
    split_list_into_three,
)
# HOW TO MAKE THE UNIT TESTS TEST THE FUNCTION IN PARTICULAR???

# Check that the split_list_into_three function splits a list of strings into
# a list of lists for every three elements in the original list.
REMOVE_TAGS_CASES = [
    # Case where the start tag is in the middle of the string.
    (["abcd<a89%justinbieber>dcba</a>"], ["abcddcba"]),
    # Case with no start tag but has an end tag.
    (["theweeknd</a>usher"],["theweekndusher"]),
    # Case where everything is encased in a start tag.
    (["<atheweeknd>", ""]),
    # A tag type that is not in the tag_types list.
    (["abc<li theweeknd>"], ["abc<li theweeknd>"]),
    # Case with extra info (\n, amp;, \xa0)
    (["abc/n<a the weeknd>", "justin bieber \xa0&amp;nicki minaj\n"],
    ["abc", "justin bieber & nicki minaj"]),
]

SPLIT_EXTEND_CASES = [
    # Case with multiple br end tags.
    (["1. All Me Whitney<br/>2. Umbrella Rihanna<br/>3. Baby Justin"],
    ["1. All Me Whitney, 2. Umbrella Rihanna, 3. Baby Justin"]),    # how to make element bs4 BeautifulSoup type
    # Case with no br end tags.
    (["1. All Me Whitney 2. Umbrella Rihanna"],
    ["1. All Me Whitney 2. Umbrella Rihanna"]),
    # Case with br tag in the beginning.
    (["</br>1. All Me Whitney</br>2. Umbrella Rihanna"],
    ["", "1. All Me Whitney", "2. Umbrella Rihanna"]),
    # Any other tests?
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
    (['2', 'Sunflower'],
    [['2', 'Sunflower']])
]

@pytest.mark.parametrize("source_text, split_text", SPLIT_LIST_CASES)
def clean_data(source_text, split_text):
    """
    Check that remove_tags() removes the information within beginning and
    end tags.

    Args:
        source_text: A list of strings representing the source text.
        split_text: A list of lists representing the strings in source_text
            grouped by three.
    """
    assert clean_data(source_text) == split_text

@pytest.mark.parametrize("source_text, split_list", SPLIT_EXTEND_CASES)
def split_and_extend(source_text, split_list):
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
    assert clean_data(source_text) == split_list

@pytest.mark.parametrize("source_text, clean_text", REMOVE_TAGS_CASES)
def clean_data(source_text, clean_text):
    """
    Check that remove_tags() removes the information within beginning and
    end tags.

    Args:
        source_text: A list of strings representing the source text.
        split_text: A list of strings representing the source text without
            tags and extraneous characters or information.
    """
    assert clean_data(source_text) == clean_text
