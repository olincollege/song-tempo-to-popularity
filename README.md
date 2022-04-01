# song-tempo-to-popularity
SoftDes 2022 Midterm: Richard Li, Natsuki Sacks, Norah Evans

This program should be able to do the following:

* Fetch the most popular songs from the Billboard Top 100
* Find the tempo/energy of those songs using Spotify's API
* Produce a visual indicating how tempo correlates with song popularity.

This program will scrape, clean, and process the BPM data only
for years 1940-2020.

The necessary data is scraped from the [Billboard Top 100](BillboardTop100of.com).

In order to scrape the data, you must download the Python Requests library. To do this, run these commands:
`pip install requests` or `python -m pip install requests`.

In order to parse the data, you must download the Beautiful Soup Python package. To do this, run this command:
`pip install beautifulsoup4`

# dependencies:
[spotipy](https://spotipy.readthedocs.io/en/2.19.0/): a lightweight spotify python wrapper.