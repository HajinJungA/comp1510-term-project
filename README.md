# COMP 1510 Term Project - Arcade

This is a Python arcade project with two games: Rock Paper Scissors and Hangman. 
Players can choose a game, play it, and save their scores.

## What is here

- `game.py`: Runs the arcade menu and manages scores.
- `rock_paper_scissors.py`: Rock Paper Scissors game.
- `hangman.py`: Hangman game.
- `scoreboard.py`: Loads and saves scores using JSON.
- `games.py`: Loads game modules.
- `tests/`: Contains pytest tests.

## The contract

A game module defines `play(player_name)`, runs exactly one session, and returns the
score as a nonnegative `int`, where higher is better. The menu is responsible for
saving the score, so games never touch the scoreboard file themselves. 
To add a new game, create a new Python module with a play(player_name) function. 
Then add the module name to GAMES in game.py.

## Games

### Rock Paper Scissors
The player chooses rock, paper, or scissors. The computer chooses randomly.
The first to win 3 rounds wins the match. Ties do not count.
The score is the number of rounds the player won (0 to 3).

### Hangman
The computer randomly selects a word with 5 to 8 letters.
The player guesses one letter at a time and has 6 incorrect guesses.
Repeated guesses and invalid inputs do not use an attempt.
The player wins by guessing the whole word before running out of attempts.
The score is the number of remaining attempts (0 to 6).

## The scoreboard

Scores are saved in `scoreboard.json` after each game and loaded when the arcade starts.

```json
{
  "rock_paper_scissors": [
    {"player": "Hajin", "score": 3}
  ],
  "hangman": [
    {"player": "Hajin", "score": 5}
  ]
}
```

If the file is missing or invalid, the arcade starts with an empty scoreboard.
The scoreboard shows the highest score for each game.

## Run it

**PyCharm:** accept the virtual environment PyCharm offers when you open the
project, and install `pytest` from the **Python Packages** panel. Then run
`game.py` to play, and right-click the `tests` folder to run the tests.

**Terminal:** From the top-level folder, set up once:

```sh
python3 -m venv .venv
```

Activate the virtual environment:

- macOS/Linux: `source .venv/bin/activate`
- Windows Git Bash: `source .venv/Scripts/activate`

Then install pytest:

```sh
python -m pip install pytest
```

Then `python game.py` plays and `python -m pytest` runs the tests.
In a new terminal, run the `activate` line again first.

## Bonus Features

None.
