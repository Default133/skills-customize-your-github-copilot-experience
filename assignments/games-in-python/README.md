
# 🎮 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Use a predefined list of words and randomly select one as the secret word for the player to guess.

#### Requirements
Completed program should:

- Randomly choose a word from a list of possible words.
- Initialize the game state, including guessed letters, remaining attempts, and the current progress display.

### 🛠️ Player Interaction and Guessing

#### Description
Allow the player to guess letters, update the displayed word progress, and prevent repeated guesses.

#### Requirements
Completed program should:

- Prompt the player to enter a letter guess.
- Show the current progress in a hidden-word format such as `_ _ _ _ _`.
- Keep track of correct and incorrect guesses.
- Prevent duplicate guesses from affecting the game state.

### 🛠️ Game Completion and Feedback

#### Description
End the game when the player guesses the word or uses all attempts, and display the final result.

#### Requirements
Completed program should:

- End when the secret word is fully guessed or the player runs out of attempts.
- Display a winning message if the player guesses the word.
- Display a losing message if the player is out of attempts.
- Reveal the secret word when the game ends.
