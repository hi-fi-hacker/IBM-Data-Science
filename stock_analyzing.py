# -*- coding: utf-8 -*-
"""Stock Analyzing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1esIRbrPxAtZjmwHYTlJwlvcdu-6iBDQz

TESLA Stock Extracting using yfinance
"""

import yfinance as yf
import pandas as pd

tesla = yf.Ticker("TSLA")

tesla_data = tesla.history(period="max")

tesla_data.reset_index(inplace=True)
tesla_data.head()

"""Plotting TESLA Chart"""

tesla_data.plot(x="Date", y="Open")

"""Game Stop Stock Extracting using yfinance"""

game_stop = yf.Ticker("GME")

game_stop_data = game_stop.history(period = "max")

game_stop_data.reset_index(inplace=True)

game_stop_data.head()

"""Plotting Game Stop Chart"""

game_stop_data.plot(x="Date", y="Open")

"""TESLA Stock Extracting using Webscraping"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

html_data = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

data = requests.get(html_data).text
print(data)

soup = BeautifulSoup(data, 'html5lib')

tesla_data = pd.DataFrame(columns=["Date", "Open"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text

    # Finally we append the data of each row to the table
    tesla_data = tesla_data.append({"Date":date, "Open":Open}, ignore_index=True)

tesla_data.tail()

"""Game Stop Stock Extracting using Webscraping"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

data = requests.get(url).text
print(data)

soup = BeautifulSoup(data, 'html5lib')

game_stop_data = pd.DataFrame(columns=["Date", "Open"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text

    # Finally we append the data of each row to the table
    game_stop_data = game_stop_data.append({"Date":date, "Open":Open}, ignore_index=True)

game_stop_data.tail()

