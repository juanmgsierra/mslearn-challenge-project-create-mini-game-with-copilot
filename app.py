import random

def game():
    choices = ['rock', 'paper', 'scissors']
    playOneMoreTime = ['yes', 'no']
    player_score = 0
    computer_score = 0

    for i in range(3):
        player_choice = input("Choose rock, paper or scissors: ")
        while player_choice not in choices:
            player_choice = input("Invalid choice. Choose rock, paper or scissors: ")

        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            player_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

    if player_score > computer_score:
        print("You win the game!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print("The game is a tie!")

    playAgain = input("Do you want to play again? (yes/no): ")
    while playAgain not in playOneMoreTime:
        playAgain = input("Invalid choice. Do you want to play again? (yes/no): ")

    if playAgain == 'yes':
        game()
    else:    
        print("Goodbye!")


game()


