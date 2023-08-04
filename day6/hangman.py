# generate a random word > find a way to make the word hidden > function run a while loop and accept a letter - if letter exists in word display that word > create a counter inside function to represent life of the hangman

import random

class Hangman:

    def __init__(self):
        self.randomWords = random.choice(['hummus', 'Beetroot', 'Tzatziki', 'Watermelon'])
        self.display = []

    def game(self):
        for i in range(len(self.randomWords)):
                self.display += '_'
        print(self.randomWords)
                
        lives = 8
        while lives > 0:
            letter = input("Choose a word: ").lower()
            for j in range(len(self.randomWords)):
                if self.randomWords[j].lower() == letter:
                    self.display[j] = letter
            
            if letter not in self.randomWords:
                lives -= 1
                print(lives)
                if lives == 0:
                    print("You lose")

            print(self.display)

            if "_" not in self.display:
                print("You Win!")
                return
        

    def __str__(self):
        return self.display


hangman = Hangman()
hangman.game()



