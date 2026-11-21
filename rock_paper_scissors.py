import random
CHOICES = ["rock", "paper", "scissors"]


def decide_winner(player: str, computer_choice: str) -> str:
    """
    Return the winner of a Rock-Paper-Scissors round.

    :param player: The player's choice of rock, paper, or scissors.
    :param computer_choice: The computer's randomly selected choice of rock,
                            paper, or scissors.
    :return: "player" if the player wins, "computer" if the computer wins,
            or "tie" if neither wins.
    """
    if player == "rock" and computer_choice == "scissors":
        return "player"
    elif player == "rock" and computer_choice == "paper":
        return "computer"
    elif player == "scissors" and computer_choice == "rock":
        return "computer"
    elif player == "scissors" and computer_choice == "paper":
        return "player"
    elif player == "paper" and computer_choice == "rock":
        return "player"
    elif player == "paper" and computer_choice == "scissors":
        return "computer"
    else:
        return "tie"


def play(player_name: str) -> int:
    """
    Play Rock-Paper-Scissors and return the player's final score.

    :param player_name: The name of the player.
    :return: The number of rounds won by the player, from 0 to 3.
    """
    score = 0
    computer_score = 0

    while True:
        while True:
            player = input(f"{player_name}'s choice: ")
            if player.lower() in CHOICES:
                break
            else:
                print("Invalid choice")
        computer_choice = random.choice(CHOICES)
        result = decide_winner(player.lower(), computer_choice)
        print(f"Computer's choice: {computer_choice}")

        if result == "player":
            score += 1
            print("You won this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer won this round!")
        elif result == "tie":
            print("It's a tie!")

        print(f"Score - {player_name}: {score}, Computer: {computer_score}")

        if score == 3:
            print("You won the match!")
            print(f"Final score - {player_name}: {score}, Computer: {computer_score}")
            return score

        elif computer_score == 3:
            print("Computer won the match!")
            print(f"Final score - {player_name}: {score}, Computer: {computer_score}")
            return score