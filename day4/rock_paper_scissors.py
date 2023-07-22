import random

class Rps:

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rps = ["rock", "paper", "scissors"]

    def announceWinner(self):
        if self.player_score == 3:
            print("Player wins game")
        elif self.computer_score == 3:
            print("Computer wins game")

        return
    
    def gameLogic(self):

        while self.player_score or self.computer_score < 3:

            computer_choice_index = random.randint(0, len(self.rps) - 1)
            computer_choice = self.rps[computer_choice_index]

            playerChoice = input("Choose rock paper or scissors: ").lower()

            if playerChoice == "rock" and computer_choice == "scissors":
                self.player_score += 1
                print(f"Computer Choice: {computer_choice}")
                print("Player wins")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "rock" and computer_choice == "paper":
                self.computer_score +=1
                print("Computer wins")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "rock" and computer_choice == "rock":
                print("Draw")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "paper" and computer_choice == "scissors":
                self.computer_score += 1
                print("Player wins")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "paper" and computer_choice == "paper":
                print("Draw")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "paper" and computer_choice == "rock":
                self.player_score += 1
                print("Player Wins")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "scissors" and computer_choice == "scissors":
                print("Draw")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "scissors" and computer_choice == "paper":
                self.player_score +=1
                print("Player Wins")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            elif playerChoice == "scissors" and computer_choice == "rock":
                self.computer_score += 1
                print("Computer Wins")
                print(f"Computer Choice: {computer_choice}")
                print(f"Computer Score: {self.computer_score}")
                print(f"Player Score: {self.player_score}")
            else:
                print("Invalid input")

        if self.player_score or self.computer_score == 3:
            self.announceWinner()    
            

game = Rps()
game.gameLogic()