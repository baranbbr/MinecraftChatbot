import meaning
import inputRefactor

refactorer = inputRefactor.InputRefactor()
meaning = meaning.Meaning()

while True:
    inpt = input("Ask me! :")
    refactored_input = refactorer.nonLetterRemover(inpt)
    refactored_input = refactorer.tokenise(refactored_input)
    print(meaning.predict(refactored_input, inpt))