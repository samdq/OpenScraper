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

print("Welcome to the program!\n")

try:
    # Read names from the "names.txt" file
    with open("names.txt", "r") as name_file:
        names = [line.strip() for line in name_file.readlines() if is_alpha(line.strip())]
except FileNotFoundError:
    print("The file 'names.txt' does not exist.")
    exit(1)

