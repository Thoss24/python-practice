import random

def play_again():
    play_again = input("Enter 'y' to play again or 'n' to exit: ")
    if play_again == 'y':
        guess()
    if play_again == 'n':
        return 
    
def setDifficulty():
    easy = 10
    hard = 5
    difficulty = input("Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return easy
    else:
        return hard

def guess():
    random_number = random.choice(range(1, 100))
    lives = setDifficulty()
    print("Guess the number between 1 - 100")
    while lives != 0:
        guess = int(input("Make a guess: "))
        lives -= 1
        if guess == random_number:
            print(f"You guessed right! The number was {random_number}")
            lives = 0
            play_again()
        elif guess < random_number:
            print("Too low. Guess again")
            print(f"You have {lives} guesses remaining\n")
        elif guess > random_number:
            print("Too high. Guess again")
            print(f"You have {lives} guesses remaining\n")
        
        if lives == 0 and guess != random_number:
            print("You lose. You ran out of guesses.")
            play_again()
        
guess()
 