# My arcade plan

## Games I chose

- Game 1: Rock-paper-scissors — Easy
- Game 2: Hangman — Medium

## Game 1: Rock-paper-scissors

- Rules, in a few sentences:
  The player plays rock-paper-scissors against the computer. The player chooses rock, paper, or scissors, and the computer chooses randomly.
  Rock beats scissors, scissors beats paper, and paper beats rock. The first one to win 3 rounds wins the game.
  If both choose the same thing, it is a tie and nobody gets a point. The game continues until someone wins 3 rounds.
- What one turn looks like:
  The player enters rock, paper, or scissors. The computer randomly chooses one of them. The game shows both choices and tells the player who won the round.
  If the player enters something invalid, the game shows an error message and asks again without counting the round.
  After each round, the game shows the current wins for both the player and computer. Then the next round starts unless someone has reached 3 wins.
- How it ends (win, lose, or out of turns):
  The game ends when either the player or the computer wins 3 rounds. The game shows who won the match and the final score.
  If the player wins 3 rounds first, the player wins. Otherwise, the computer wins.
- How a score is earned (the formula or rule, and why higher is better):
  The player gets 1 point for each round they win. Losing or tying a round does not give any points.
  The final score is the total number of rounds the player won, from 0 to 3. A higher score means the player won more rounds.
  The game returns the final score as an integer to the arcade menu.
- Game settings (the fixed numbers or choices that define the game, such as
  grid size, number of guesses, word length, or question count):
  The player can choose rock, paper, or scissors. The computer randomly chooses one of these three options.
  The game continues until either the player or the computer wins 3 rounds. Ties do not count as wins, and there is no limit on the number of ties.

## Game 2: Hangman

- Rules, in a few sentences:
  The player has to guess a hidden word by entering one letter at a time. The word is randomly selected from a list of English words with 5 to 8 letters.
  If the player guesses a correct letter, all matching letters in the word are revealed. If the guess is wrong, the player loses one attempt.
  The player has 6 chances to make wrong guesses. The goal is to guess the whole word before running out of chances.
- What one turn looks like:
  The game shows the hidden word as underscores and asks the player to enter one letter.
  If the letter is in the word, all matching letters are revealed. If it is wrong, the number of remaining attempts decreases by 1.
  If the player enters an invalid input or a letter they already guessed, the game shows a message and asks again without losing an attempt. Uppercase and lowercase letters are treated the same.
  After each valid guess, the game shows the updated word and the number of attempts remaining.
- How it ends (win, lose, or out of turns):
  The player wins if they guess the whole word before making 6 wrong guesses.
  The player loses if they make 6 wrong guesses before completing the word.
  When the game ends, it shows whether the player won or lost, reveal the full word, and displays the final score.
- How a score is earned (the formula or rule, and why higher is better):
  The player's score is the number of wrong guesses remaining when the game ends.
  The player starts with 6 attempts and loses 1 for each wrong guess. For example, if the player wins with 2 wrong guesses, the final score is 4.
  If the player loses all 6 attempts, the score is 0. The maximum score is 6, and a higher score means the player made fewer mistakes.
  The game returns the final score as an integer to the arcade menu.
- Game settings (the fixed numbers or choices that define the game, such as
  grid size, number of guesses, word length, or question count):
  The game uses a built-in list of English words with 5 to 8 letters. Each word contains only letters, with no spaces, numbers, or special characters.
  One word is randomly selected at the start of each game. The player can make up to 6 wrong guesses.
  The game accepts both uppercase and lowercase letters. Invalid inputs and repeated guesses do not reduce the remaining attempts.

## Scoreboard fields

The arcade uses one `scoreboard.json` file to save scores from both games.
Each game has its own key, `rock_paper_scissors` and `hangman`. Each key contains a list of records with the player's name (`player`) and final score (`score`).
The player name is a string, and the score is an integer. After each completed game, the arcade adds a new record and saves the scoreboard. The scores are kept even after the program closes.

Example:
```json
{
  "rock_paper_scissors": [
    {"player": "Sam", "score": 3}
  ],
  "hangman": [
    {"player": "Alex", "score": 4}
  ]
}
```