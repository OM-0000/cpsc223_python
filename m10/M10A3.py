# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 10 Assignment 3

from bs4 import BeautifulSoup
import requests

hostName = input("What is the hostname? ")
allgood = False
#Let's just go on a quick tangent to make sure the url is valid (https:// OR http:// is included)
allgood = hostName.startswith('http://') or hostName.startswith('https://')

if not allgood:
    #let's just assume the user left off the scheme/protocol for an otherwise valid url
    hostName = 'https://' + hostName
    allgood = True

if allgood:
    try:
        page = requests.get(hostName)
        doc = BeautifulSoup(page.content, "html.parser")
        print(doc.prettify())
    except requests.exceptions.ConnectionError as e1:
        print("Could not connect to that url")