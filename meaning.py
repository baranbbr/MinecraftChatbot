import numpy as np

import urllib.request, json

class Meaning:
    """By passing refactored input this class calculate the meaning of sentence
       Simple algorithm will predict what user want to know
    """
    def __init__(self):
        self.classifier_words = {
            "Craft_question": ['how', 'do', 'does,', 'would', 'can', 'could',
                               'i', 'is', 'be', 'was', 'were', 'to', 'been',
                               'craft', 'crafted', 'make', 'made',
                               'solution', 'recipe',
                               'know', 'about'],
            "Item_question":  ['what', 'can', 'could',
                               'i', 'is', 'be',
                               'do', 'did', 'done', 'like', 'for', 'used',
                               'with'],
            "Greeting":       ['hi', 'hello', 'good', 'morning', 'afternoon', 'yo',
                               'hey']
        }

        self.items_names = list()
        with urllib.request.urlopen("http://minecraft-ids.grahamedgecombe.com/items.json") as url:
            data = json.loads(url.read().decode())
            for item in data:
                self.items_names.append(item['name'].lower())

    def predict(self, refactored_sentence, unrefactored_sentence):
        """returns list of sentence type, minecraft item name, and confidence of prediction (percentage)"""
        max_local = 0
        max_global = 0
        final_type = None
        confidence1 = 0
        confidence2 = 0
        for key in self.classifier_words:
            for word in refactored_sentence[0]:
                if word[0] in self.classifier_words.get(key):
                    max_local = max_local + 1 + word[1]
            if max_local > max_global:
                confidence2 = confidence1
                confidence1 = max_local - max_global
                max_global = max_local
                final_type = key
            max_local=0

        item_name = None
        for item in self.items_names:
            if item in unrefactored_sentence:
                item_name = item
                break

        confidence_percentage = 100
        if confidence2 is not 0:
            confidence_percentage = confidence_percentage - confidence1*100/confidence2
        return final_type, item_name, confidence_percentage
