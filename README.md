# song-tempo-to-popularity
SoftDes 2022 Midterm: Richard Li, Natsuki Sacks, Norah Evans

In this repository lives a program that should be able to do the following:

* Fetch the most popular songs from the Billboard Top 100 from 1940-2019
* Find the tempo of those songs using Spotify's API
* Produce a visual indicating how tempo correlates with song popularity over time.

This program will scrape, clean, and process the BPM data only for years 1940-2019.

The necessary data is scraped from the [Billboard Top 100](BillboardTop100of.com).


## dependencies:

In order to scrape the data, you must install the Python Requests library. To do this, run these commands:
`pip install requests` or `python -m pip install requests`.

In order to parse the data, you must instal the Beautiful Soup Python package. To do this, run this command:
`pip install beautifulsoup4`

In order to query Spotify's Web API, you must install [spotipy](https://spotipy.readthedocs.io/en/2.19.0/). To do this, run this command: 
`pip install spotipy`

In order to analyze the data we scraped, you must install Pandas. To do this, run this command:
`pip install pandas`

In order to visualize the data we analyzed, you must install Matplotlib. To do this, run this command:
`python -m pip install -U matplotlib`

## Running code:
Note that in order to get any data from Spotify, you'll have to get a secret API key from [Spotify](https://developer.spotify.com/dashboard/login).
After doing this, you'll have to put that in a yaml file called `config.yaml` as indicated in `bpm.py`. Do so with the following formatting:

    SPOTIPY_CLIENT_ID : [ENTER SPOTIPY CLIENT ID HERE]
    SPOTIPY_CLIENT_SECRET : [ENTER SPOTIPY CLIENT SECRET HERE]

Afterwards, you can run each of the three files (`billboard.py` || `bpm.py` || `visualization.py`) in succession. 

You will find that billboard.py produces a csv called `top100.csv` containing a csv file of lists. It should be formatted as follows: [rank, track, artist]

You will find that bpm.py produces 2 csvs called `bpm.csv` and `bpm2.csv` containing tempo information for all of the Billboard Top 100 songs between 1940 and 2019. 

*note, we scraped data for 2020 as well, but for ease of visualization by decade, we only used up to 2019*

You will find that visualization.py produces 3 graphs that each illustrate something different about the data we scraped.

Happy spotipying!