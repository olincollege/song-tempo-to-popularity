"""
Test that the functions in billboard_functions.py are working properly.

There is no function test for creating the final list of lists of music data
for years 1940, 1942-1944, 2013, and 2015-2020. This is because these years
contained more messy and complexly parsed data that needed a little more
cleaning than the years that could simply use the complete_billboard
function to generate the final list of lists of cleaned music data.
"""

import collections
import pytest
from billboard_functions import (
    get_data,
    remove_long_tags,
    split_list_into_three,
    import_to_df,
    complete_billboard
)
# HOW TO MAKE THE UNIT TESTS TEST THE FUNCTION IN PARTICULAR???

# Check that the split_list_into_three function splits a list of strings into
# a list of lists for every three elements in the original list.
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

# get_data() cannot be tested.

# HOW TO TEST IMPORT_TO_DF()?

REMOVE_TAGS_CASES = [
    # Case where the start tag is in the middle of the string.
    ("abcd<a89%justinbieber>dcba</a>", "abcddcba"),
    
]