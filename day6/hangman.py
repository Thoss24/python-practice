# generate a random word > find a way to make the word hidden > function run a while loop and accept a letter - if letter exists in word display that word > create a counter inside function to represent life of the hangman

import random

class Hangman:

    def __init__(self):
        self.word = ''
        self.display = []

    def randomWord(self):
        word_list = ['ardvark', 'lemming', 'crocodile', 'kangaroo']
        random_word = random.choice(word_list)
        self.word = random_word
        for _ in range(len(random_word)):
            self.display += "_"
    
    def checkWord(self):
        lives = 8
        while lives > 0:
            print(self.display)
            letter = input("Choose letter: ").lower()
            for position in range(len(self.word)):
                if letter ==  self.word[position]:
                    self.display[position] = letter
            
            if letter not in self.word:
                lives -= 1

            if ' '.join(self.display) == self.word:
                print("You Win!")
            elif lives == 0:
                print("You lose!")
    
hangman = Hangman()
hangman.randomWord()
hangman.checkWord()
    


