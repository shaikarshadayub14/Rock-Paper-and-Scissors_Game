import random

def get_user_choice():
    """
    Function to get and validate user choice for Rock, Paper, Scissors.
    """
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    while True:
        try:
            user_choice = int(input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): "))
            if user_choice in choices:
                return choices[user_choice]
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_computer_choice():
    """
    Function to randomly generate computer's choice for Rock, Paper, Scissors.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the round.
    Returns 0 if it's a tie, 1 if user wins, 2 if computer wins.
    """
    if user_choice == computer_choice:
        return 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return 1
    else:
        return 2

def print_result(user_choice, computer_choice, result):
    """
    Function to print the result of each round.
    """
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    elif result == 2:
        print("Computer wins!")

def play_game():
    """
    Function to play the Rock, Paper, Scissors game.
    """
    user_score = 0
    computer_score = 0
    round_number = 1
    play_again = True
    
    while play_again:
        print(f"\nRound {round_number}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)
        
        if result == 1:
            user_score += 1
        elif result == 2:
            computer_score += 1
        
        print(f"\nScoreboard - You: {user_score}, Computer: {computer_score}")
        
        round_number += 1
        while True:
            again = input("\nDo you want to play again? (yes/no): ").lower()
            if again == "no":
                play_again = False
                break
            elif again == "yes":
                break
            else:
                print("Invalid input! Please enter yes or no.")

    print("\nThanks for playing!")

# Start the game
play_game()
