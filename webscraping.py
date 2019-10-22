import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.minecraftcraftingguide.net'
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, "html.parser")
# found = soup.find_all("img")
# print(found)

item = "wood"
item_regex = r"\b"+item+r"\b"
# Find how to craft item
for i in range(0, len(soup.find_all('img')) + 1):
    try:
        data = soup.find_all('img')[i]
        # print(data)
        img_title = data['alt']
        print("img title is => " + str(img_title))
        img_link = data['src']
        contains_item = re.compile(item_regex, re.IGNORECASE)
        contains_crafting = re.compile('crafting', re.IGNORECASE)
        if contains_item.search(img_title) and contains_crafting.search(img_title):
            print("je suis " + str(img_title))
            print("This is how to craft a", item, "http://" + str(img_link)[2:])
            break
    except IndexError:
        print(str(item) + " could not be found")


# What can I do with item?
# Need to look at ingredients then possibly span?
# for i in range(0, len(soup.find_all(item))+1):
#     try:
#         data = soup.find_all(item)[i]
#         print(data)
#     except IndexError:
#         print("error")