import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(options)

    player_choice = input("Enter a choice (rock,paper, or scissors): ")
    computer_choice = cpu_choice

    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose: {player}, The computer chose: {computer}")
    if player == computer:
        return "Its a tie!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win!"
        else:
            return "Paper covers Rock! you loose!"

    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts Paper! you loose!"
        else:
            return "Paper covers Rock! you win!"

    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! you loose!"
        else:
            return "Scissors cuts paper! you win!"


choices = get_choices()

p_choice = choices["player"]
c_choice = choices["computer"]

result = check_win(p_choice, c_choice)

print(result)