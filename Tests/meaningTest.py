import unittest
import inputRefactor
import meaning

refactorer = inputRefactor.InputRefactor()
meaning = meaning.Meaning()


class MeaningTesting(unittest.TestCase):

    def setUp(self):
        self.item_questions = [
            "What can I do with air?",
            "What can I do with jungle wood planks?",
            "What is Black Dye for?",
            "What to do with break?",
            "Is Golden Hoe for cutting wood?",
            "What can I do with iron nugget?",
            "What is Coal used for?"
        ]
        self.carfting_questions = [
            "What can I craft from 2 jungle planks?",
            "How to make air?",
            "How to create jungle wood planks?",
            "What could have been made from 4 golden nuggets?",
            "How does Chainmail Helmet is made?",
            "Tell me recipe for crafting cooked chicken?",
            "Tell me solution fro Bow"
        ]

    def test_item_questions(self):
        for question in self.item_questions:
            response_ref = refactorer.nonLetterRemover(question)
            response_ref = refactorer.tokenise(response_ref)
            response_list = meaning.predict(response_ref, question)
            self.assertTrue(response_list[0] == 'Item_question')

    def test_crafting_question(self):
        for question in self.carfting_questions:
            response_ref = refactorer.nonLetterRemover(question)
            response_ref = refactorer.tokenise(response_ref)
            response_list = meaning.predict(response_ref, question)
            self.assertTrue(response_list[0] == 'Craft_question')


if __name__ == '__main__':
    unittest.main()
