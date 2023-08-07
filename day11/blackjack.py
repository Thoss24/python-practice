import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def drawCard():
    card = random.choice(cards)
    return card

def playAgain():
    play_again = input("Press 'y' to play again and 'n' to exit game: ").lower()
    return play_again

def game():
    dealer_hand = []
    player_hand = []

    game_over = False

    game_start = input("Welcome to the table! Enter 'play' to begin the game: ").lower()

    if game_start == 'play':
        player_first_card = drawCard()
        player_hand.append(player_first_card)
        dealer_first_card = drawCard()
        dealer_second_card = drawCard()
        dealer_hand.append(dealer_first_card)
        dealer_hand.append(dealer_second_card)
        print(f"Your cards: {player_hand}")
        print(f"Dealer cards: {[dealer_hand[0], '?']}")

    while game_over is False:
        get_another_card = input("Type 'y' for another card or 'n' to pass: ")
        if get_another_card == 'y':
            player_card = drawCard()
            if player_card == 11:
                ace_choice = int(input("You drew and Ace, type '11' for 11 or '1' for 1: "))
                if ace_choice == 1:
                    player_card = 1
            player_hand.append(player_card)
            print(f"Your cards: {player_hand}")

        else:
            if sum(player_hand) > sum(dealer_hand):
                print(f"You win!")
                print(f"Your hand total {sum(player_hand)} is greater than the dealer hand total {sum(dealer_hand)}")
                play_again = playAgain()
                if play_again == 'y':
                    game_over = True
                    game()
                else:
                    return
            else:
                print(f"You lose!")
                print(f"Your hand total {sum(player_hand)} is less than the dealer hand total {sum(dealer_hand)}")
                if play_again == 'y':
                    game_over = True
                    game()
                else:
                    return

        if sum(player_hand) == 21:
            print("You win!!")
            print(f"Your hand {player_hand}")
            play_more = playAgain()
            if play_more == 'y':
                game_over = True
                game()
            else:
                return

        elif sum(player_hand) > 21:
            print(f"You lose! your hand is greater than 21: {player_hand}")
            play_again = playAgain()
            if play_again == 'y':
                game_over = True
                game()
            else:
                return
            
        elif sum(player_hand) == sum(dealer_hand):
            print("It's a draw")
            print(f"Your hand {player_hand}")
            print(f"Dealer hand {dealer_hand}")
        

game()


