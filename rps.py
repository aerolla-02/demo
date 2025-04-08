import random
import os

def clear_screen():
    # Clear the terminal screen (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    options = ["rock", "paper", "scissors"]
    
    while True:
        clear_screen()

        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter your choice (rock, paper, scissors): ").lower()

        print(f"\nYou chose {player}.")
        print(f"Computer chose {computer}.")

        if player == computer:
            print("It's a Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            clear_screen()
            print("Thanks for playing!")
            break

play_game()
