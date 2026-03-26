class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+'('+self.meaning+')'

flash = []
print("welcome to flashcard application. ")

while(True):
    word = input("Enter the word you want input on the flashcard: ")
    meaning = input("Enter the meaning of that word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to add another flashcard if not enter 1: "))

    if(option):
        break


print("\n your flashcards. ")
for i in flash:
    print(">" , i)