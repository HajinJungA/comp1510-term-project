import random


WORDS = [
    "apple",
    "banana",
    "orange",
    "grape",
    "cherry",
    "lemon",
    "peach",
    "melon",
    "carrot",
    "potato",
    "tomato",
    "rabbit",
    "turtle",
    "pencil",
    "computer"
]
VALID_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def choose_word() -> str:
    """
    Return a randomly selected word from the WORDS list.

    :return: A randomly selected word from WORDS.
    """
    return random.choice(WORDS)


def display_word(word: str, guessed_letters: list[str]) -> str:
    """
    Return a string showing guessed letters and hiding the others.

    :param word: The word selected by choose_word().
    :param guessed_letters: A list of letters the player has guessed.
    :return: A new string with guessed letters revealed and
             unguessed letters replaced by underscores.
    """
    displayed_word = ""

    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    return displayed_word.strip()


def is_word_guessed(word: str, guessed_letters: list[str]) -> bool:
    """
    Check whether all letters in the word have been guessed.

    :param word: The word selected by choose_word().
    :param guessed_letters: A list of letters the player has guessed.
    :return: True if all letters have been guessed, otherwise False.
    """
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def play(player_name: str) -> int:
    """
    Play Hangman and return the player's final score.

    :param player_name: The name of the player.
    :return: The number of remaining incorrect guesses allowed, from 0 to 6.
    """
    attempts_remaining = 6
    guessed_letters = []
    word = choose_word()

    print(f"Welcome to Hangman, {player_name}!")

    while True:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ")

        if guess.lower() in guessed_letters:
            print("You already guessed that letter.")
        elif len(guess) == 1 and guess in VALID_LETTERS:
            guessed_letters.append(guess.lower())
            if guess.lower() not in word:
                attempts_remaining -= 1
        else:
            print("Invalid input. Enter one English letter.")

        print(f"Attempts remaining: {attempts_remaining}")

        if is_word_guessed(word, guessed_letters):
            print("You won the game!")
            break

        if attempts_remaining == 0:
            print("You lost the game!")
            break

    print(f"The word was: {word}")
    return attempts_remaining