from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as file_object:
    doc = BeautifulSoup(file_object, "html.parser")

#print(doc.prettify())

tag = doc.title
print(tag.string)

#modify the tag
tag.string = "hello"
#print(doc)


#finding all tags
tags = doc.find_all("p")[0]
print(tags.find_all("b"))


#--------------------------Accessing websites----------------------------------------------
url = "https://www.newegg.ca/gigabyte-gv-n308tgaming-oc-12gd-geforce-rtx-3080-ti-12gb-graphics-card-windforce-3x/p/N82E16814932436?cm_re=3080-_-14-932-436-_-Product&Description=3080"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())

prices = doc.find_all(string="$")
print(prices)

try:
    parent = prices[0].parent
    print(parent)
    strong = parent.find("strong")
    print(strong.string)
except IndexError:
    print("Didn't find any matches.")