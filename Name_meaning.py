import requests
from bs4 import BeautifulSoup as bs
import random
import os

# Function to check if a string is alpha
def is_alpha(s):
    return s.isalpha()

# Function to fetch the meaning of a name
def fetch_name_meaning(name):
    url = "https://www.thenamemeaning.com/"
    url = url + name + "/"
    r = requests.get(url)
    data = r.content
    soup = bs(data, "lxml")
    try:
        meaning = soup.strong.next_sibling.strip()
        return meaning
    except:
        return "Not found"

