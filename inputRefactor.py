import numpy as np
import nltk

#uncomment this lines if you have an error with punkt
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import PunktSentenceTokenizer

class inputRefactor:

    @classmethod
    def nonLetterRemover(self, sentence):
        '''Removes Unecessary Commas and Determines if it is a question'''
        exclusion_characters = [";",":","!","!","#",",",".","@","'","£","$","%","^","&","*","(",")","\"","{","}","]","[","~","¬","`"]
        new_sentence_array = []
        is_question = False  # initialising is_question as false
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
    def tokenise(self, sentence):
        '''Stores Data in 2D array to determine its ID and amount of times it occurs'''
        is_question = sentence[1]
        sentence = sentence[0] #splitting input
        word = []
        times = []
        while len(sentence)>0:
            word_count = 0
            temp_word = sentence[0]
            sentence_constant = sentence
            for j in sentence_constant: #getting all unique words
                if temp_word == j:
                    sentence.remove(j)
                    word_count += 1
            word.append(temp_word)
            times.append(word_count)
        data_store = np.zeros(len(word), dtype={'names': ('word', 'times'),
                                        'formats': ('U46', 'i4')})  # initialising data store with formats of data types.
        data_store['word'] = word
        data_store['times'] = times # adding all unique words and their occurrence to an associative array
        return data_store, is_question

    @classmethod
    def classifyWords(self, word_array):
        '''Adds word-type (noun,verb) to existing 2D array format'''
        is_question = word_array[1]
        word_array = word_array[0]
        word= []
        times = []
        data_store = np.zeros(len(word_array), dtype={'names': ('word', 'times','types'),
                                               'formats': ('U46', 'i4', 'U46')})
        count = 0
        while len(word_array) > count:
            word.append(word_array['word'][count])
            times.append(word_array['times'][count])
            count+= 1
        types = inputRefactor.processWordType(word)
        data_store['word'] = word
        data_store['types'] = types
        data_store['times'] = times #adding all unique words and their occurrence to an associative array
        return data_store, is_question

    @classmethod
    def processWordType(self, sentence): #takes sentence inputs and finds word type
        type_list= []
        red_dict = {"CC":"NULL","CD":"NULL","DT":"NULL","EX":"NULL","FW":"NULL","IN":"NULL","JJ":"ADJECTIVE",
                   "JJR":"ADJECTIVE","JJS":"ADJECTIVE","LS":"NULL","MD":"NULL","NN":"NOUN","NNS":"NOUN",
                   "NNP":"NOUN","NNPS":"NOUN","PDT":"NULL","POS":"NULL","PRP":"PERSONAL","PRP$":"PERSONAL",
                   "RB":"ADVERB","RBR":"ADVERB","RBS":"ADVERB","RP":"ADVERB","TO":"NULL","UH":"NULL",
                   "VB":"VERB","VBD":"VERB","VBG":"VERB","VBN":"VERB","VBP":"VERB","VBZ":"VERB","WDT":
                   "PRONOUN","WP":"PRONOUN","WP$":"PRONOUN","WRB":"PRONOUN"} #dictionary of reference for codes, useless ones set to NULL
        for i in sentence:
            words = nltk.word_tokenize(i) #setting each word to the NLTK ID
            tagged = nltk.pos_tag(words) #getting the code associated with the ID
            type_list.append(red_dict[tagged[0][1]]) #adding the referenced word in the dic above to an array
        return(type_list)


