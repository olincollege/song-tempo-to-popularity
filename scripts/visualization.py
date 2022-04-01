"""
This file contains all the functions that are necessary to visualize the data.
"""
import pandas as pd
import matplotlib.pyplot as plt

def yearvsbpm():
    """
    This function reads data from bpmFULL.csv and averages the bpm from each
    year. It then plots average BPM in the year against the year to derive a
    possible trend.
    This function has no inputs necessary to call it.
    This function outputs a line graph that represents the Average BPM vs Year.
    """
    dataframe=pd.read_csv("data/bpmFULL.csv")
    mean_data = dataframe.mean(axis = 0).reset_index()
    mean_data.columns = ['year', 'mean']
    plt.plot(mean_data["year"].astype(int), mean_data["mean"])
    plt.xlabel("Year")
    plt.ylabel("Average BPM")
    plt.title("Average BPM vs Year")
    plt.show()

def scatterplot():
    """
    This function reads data from bpm.csv moves it into an array for each
    decade. It then plots each song in the top 100 against it's bpm to derive a
    possible trend.
    This function has no inputs necessary to call it.
    This function outputs a scatter plot that represents the Average BPM vs
    Popularity vs Decade.
    """
    df2 = pd.read_csv("data/bpm.csv")
    data = [df2['Unnamed: 0'], df2['Unnamed: 0'], df2['Unnamed: 0'],
    df2['Unnamed: 0'], df2['Unnamed: 0'], df2['Unnamed: 0'], df2['Unnamed: 0'],
    df2['Unnamed: 0'], df2['Unnamed: 0'], df2['Unnamed: 0']]
    forties_data = [df2['1940'], df2['1941'], df2['1942'], df2['1943'],
    df2['1944'], df2['1945'], df2['1946'], df2['1947'],df2['1948'],df2['1949']]
    fifties_data = [df2['1950'], df2['1951'], df2['1952'], df2['1953'],
    df2['1954'], df2['1955'], df2['1956'], df2['1957'], df2['1958'],df2['1959']]
    sixties_data = [df2['1960'], df2['1961'], df2['1962'], df2['1963'],
    df2['1964'], df2['1965'], df2['1966'], df2['1967'], df2['1968'],df2['1969']]
    seventies_data = [df2['1970'], df2['1971'], df2['1972'], df2['1973'],
    df2['1974'], df2['1975'], df2['1976'], df2['1977'], df2['1978'],df2['1979']]
    eighties_data = [df2['1980'], df2['1981'], df2['1982'], df2['1983'],
    df2['1984'], df2['1985'], df2['1986'], df2['1987'], df2['1988'],df2['1989']]
    nineties_data = [df2['1990'], df2['1991'], df2['1992'], df2['1993'],
    df2['1994'], df2['1995'], df2['1996'], df2['1997'], df2['1998'],df2['1999']]
    twothousand_data = [df2['2000'],df2['2001'],df2['2002'],df2['2003'],
    df2['2004'],df2['2005'], df2['2006'],df2['2007'],df2['2008'],df2['2009']]
    twentytens_data = [df2['2010'],df2['2011'],df2['2012'],df2['2013'],
    df2['2014'],df2['2015'],df2['2016'],df2['2017'],df2['2018'],df2['2019']]
    plt.scatter(data,forties_data, c = 'red', label = '1940s')
    plt.scatter(data,fifties_data, c = 'orange', label = '1950s')
    plt.scatter(data,sixties_data, c = 'yellow', label = '1960s')
    plt.scatter(data,seventies_data, c = 'green', label = '1970s')
    plt.scatter(data,eighties_data, c = 'blue', label = '1980s')
    plt.scatter(data,nineties_data, c = 'purple', label = '1990s')
    plt.scatter(data,twothousand_data, c = 'pink', label = '2000s')
    plt.scatter(data,twentytens_data, c = 'grey', label = '2010s')
    plt.legend(loc='upper left')
    plt.xlabel("Ranking on Billboard")
    plt.ylabel("Average BPM")
    plt.title("Average BPM vs Popularity for Each Decade")
    plt.show()

def popularityvsbpm():
    """
    This function reads data from bpmFULL.csv and averages the bpm from each
    rank. It then plots average BPM in the rank against it's popularity to derive a possible trend.
    This function has no inputs necessary to call it.
    This function outputs a line graph that represents the Average BPM vs Popularity.
    """
    df3=pd.read_csv("data/bpmFULL.csv")
    mean_data = df3.mean(axis = 1).reset_index()
    mean_data.columns = ['popularity', 'mean']
    plt.plot(mean_data["popularity"], mean_data["mean"])
    plt.xlabel("Ranking on Billboard")
    plt.ylabel("Average BPM")
    plt.title("Average BPM vs Popularity")
    plt.show()
scatterplot()
