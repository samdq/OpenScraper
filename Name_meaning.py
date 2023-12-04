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

for i in range(0,50):
    # Select a random name from the list of names
    random_name = random.choice(names)
    rd = random.randint(1,30) #random date
    rm = random.randint(2,8)  #random month

    # Fetch the meaning of the random name
    name_meaning = fetch_name_meaning(random_name)

    print(f"The meaning of the name '{random_name}' is: {name_meaning}")

    # Write the name and its meaning to "output.txt"
    with open("output.txt", "w") as output_file:
        output_file.write(f"Name: {random_name}, Meaning: {name_meaning}\n")
        os.system("git pull origin master")
        os.system("git add output.txt")
        os.system(f'git commit --amend --date="2023-0{rm}-{rd}" --no-edit')
        os.system('git push -u origin master')
