class GetWebInfo:
    import re
    import requests
    from bs4 import BeautifulSoup

    def __init__(self):
        url = 'https://www.minecraftcraftingguide.net'
        response = self.requests.get(url)
        self.soup = self.BeautifulSoup(response.text, "html.parser")

    def get_craft_info(self, item):
        item_regex = r"\b" + item + r"\b"
        # Find how to craft item
        for i in range(0, len(self.soup.find_all('img')) + 1):
            try:
                data = self.soup.find_all('img')[i]
                # print(data)
                img_title = data['alt']
                img_link = data['src']
                contains_item = self.re.compile(item_regex, self.re.IGNORECASE)
                contains_crafting = self.re.compile('crafting', self.re.IGNORECASE)
                if contains_item.search(img_title) and contains_crafting.search(img_title):
                    return str(img_link)[2:]
            except IndexError:
                print(str(item) + " could not be found")
