import random

def get_choice():
    choices = ["rock", "paper", "scissor"]
    while True:
        user = input("Your choice (rock/paper/scissor): ").lower()
        if user in choices:
            return user
        else:
            print("Invalid input! Please try again.")

def determine_winner(user, comp):
    if user == comp:
        return "tie"
    else:
        if user == "rock":
            if comp == "scissor":
                return "user"
            else:
                return "computer"
        elif user == "paper":
            if comp == "rock":
                return "user"
            else:
                return "computer"
        elif user == "scissor":
            if comp == "paper":
                return "user"
            else:
                return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_choice()
        comp = random.choice(["rock", "paper", "scissor"])
        print("Computer chose:", comp)

        result = determine_winner(user, comp)
        if result == "tie":
            print("It's a tie.")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("Score => You:", user_score, "| Computer:", computer_score)

        again = input("Do you want to play another round? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

play_game()
