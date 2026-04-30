class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        
    def __str__(self):
        return self.word + ' ( ' + self.meaning+' ) '
    
flash = []
print("Welcome to Flashcard game")

while True:
    word = input("Enter a word :")
    meaning = input("Enter a meaning :")

    flash.append(Flashcard(word, meaning))
    option = int(input("Enter 0, if you want to print another Flashcard else enter 1 :"))

    if option:
        break

print("Your Flashcards")
for i in flash:
    print(">", i)