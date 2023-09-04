import random

def get_choices():
    player_choice = input("Enter a choice (Rock , paper, sciossors) ")
    options = ["Rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}

    return choices

def check_win(player, computer):
    print("you chose " + player + ", computer chose " + computer)
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock beats scissors! You win!"
        else:
            return "Paper covers Rock! You lose."
    elif player == "paper":
        if computer == "Rock":
            return "Paper beats scissors! You win!"
        else:
            return "Scissors beats paper! You lose."
    elif player == "Scissors":
        if computer == "paper":
            return "Scissors beats Paper! You win!"
        else:
            return "Rock beats Scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)