import numpy as np


class InputRefactor:

    @classmethod
    def nonLetterRemover(cls, sentence):
        '''Removes Unecessary Commas and Determines if it is a question'''
        exclusion_characters = [";", ":", "!", "!", "#", ",", ".", "@", "'", "£", "$", "%", "^", "&", "*", "(", ")",
                                "\"", "{", "}", "]", "[", "~", "¬", "`"]
        new_sentence_array = []
        is_question = False  # initialising isQuestion as false
        sentence = sentence.lower()
        for word in sentence.split():  # getting each word individually
            new_word_array = []
            for letter in word:
                if letter == "?":
                    is_question = True  # checking whether it contains a question
                elif letter in exclusion_characters:
                    pass
                else:
                    new_word_array.append(letter)
            new_word_array = ''.join(new_word_array)  # reconstructing inputs without strange characters
            new_sentence_array.append(new_word_array)
        return new_sentence_array, is_question

    @classmethod
    def tokenise(cls, sentence):
        '''Stores Data in 2D array to determine its ID and amount of times it occurs'''
        is_question = sentence[1]
        sentence = sentence[0]  # splitting input
        word = []
        times = []
        while len(sentence) > 0:
            word_count = 0
            temp_word = sentence[0]
            sentence_constant = sentence
            for j in sentence_constant:  # getting all unique words
                if temp_word == j:
                    sentence.remove(j)
                    word_count += 1
            word.append(temp_word)
            times.append(word_count)
        data_store = np.zeros(len(word), dtype={'names': ('word', 'times'),
                                                'formats': (
                                                    'U46',
                                                    'i4')})  # initialising data store with formats of data types.
        data_store['word'] = word
        data_store['times'] = times  # adding all unique words and their occurrence to an associative array
        return data_store, is_question
