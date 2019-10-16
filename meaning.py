class Meaning:
    """By passing refactored input this class calculate the meaning of sentence
       Simple algorithm will predict what user want to know
    """
    def __init__(self):
        self.classifier_words = {
            "Craft_question": ['how', 'do', 'does,', 'would', 'can', 'could',
                               'I', 'is', 'be', 'was', 'were', 'to',
                               'craft', 'crafted', 'make', 'made',
                               'solution', 'recipe',
                               'know', 'about'],
            "Item_question":  ['what', 'can', 'could',
                               'I', 'is', 'be',
                               'do', 'did', 'done',
                               'with'],
            "Greeting":       ['Hi', 'Hello', 'Good', 'Morning', 'Afternoon', 'Yo',
                               'Hey']
        }

    def predict(self, sentence_words, sentence_words_count):
        max_local = 0
        max_global = 0
        final_type = None
        confidence = 0
        for key in self.classifier_words:
            iterator = 0
            for word in sentence_words:
                if word in self.classifier_words.get(key):
                    max_local = max_local + 1 + sentence_words_count[iterator]
                iterator = iterator + 1
            if max_local > max_global:
                confidence = max_local - max_global
                max_global = max_local
                final_type = key
        return final_type, confidence

meaning = Meaning()
print(
meaning.predict(
    ["How", "to", "create", "axe"],
    [1,1,1,1]
)
)