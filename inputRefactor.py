import numpy as np


class InputRefactor:

    @classmethod
    def nonLetterRemover(self, sentence):
        '''Removes Unecessary Commas and Determines if it is a question'''
        exclusionCharacters = [";", ":", "!", "!", "#", ",", ".", "@", "'", "£", "$", "%", "^", "&", "*", "(", ")",
                               "\"", "{", "}", "]", "[", "~", "¬", "`"]
        newSentenceArray = []
        isQuestion = False  # initialising isQuestion as false
        sentence = sentence.lower()
        for word in sentence.split():  # getting each word individually
            newWordArray = []
            for letter in word:
                if letter == "?":
                    isQuestion = True  # checking whether it contains a question
                elif letter in exclusionCharacters:
                    pass
                else:
                    newWordArray.append(letter)
            newWordArray = ''.join(newWordArray)  # reconstructing inputs without strange characters
            newSentenceArray.append(newWordArray)
        return newSentenceArray, isQuestion

    @classmethod
    def tokenise(self, sentence):
        '''Stores Data in 2D array to determine its ID and amount of times it occurs'''
        isQuestion = sentence[1]
        sentence = sentence[0]  # splitting input
        word = []
        times = []
        uniqueCount = 0
        while len(sentence) > 0:
            wordCount = 0
            tempWord = sentence[0]
            sentenceConstant = sentence
            for j in sentenceConstant:  # getting all unique words
                if tempWord == j:
                    sentence.remove(j)
                    wordCount += 1
            word.append(tempWord)
            times.append(wordCount)
        dataStore = np.zeros(len(word), dtype={'names': ('word', 'times'),
                                               'formats': (
                                               'U46', 'i4')})  # initialising data store with formats of data types.
        dataStore['word'] = word
        dataStore['times'] = times  # adding all unique words and their occurrence to an associative array
        return dataStore, isQuestion
