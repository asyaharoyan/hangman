# HANGMAN FOR PROGRAMMERS

Hangman for programmers is a terminal game done by using Python.
The player has 6 attempts to guess the word. With each word there is a shoer introduction to help the player to guess the right letters.

Here is the live version of the game: 
[HANGMAN FOR PROGRAMMERS](https://hangman-for-programmers-1e8bf1b491a5.herokuapp.com/)

![Screenshot of the game](media/hangman.png)

## How to play

Hangman for programmers is a game based on the classic hangman game. 

The words are programming related. Each word has a short description to help the player to guess. 

The player has 6 attempts to fail. If they don't guess the word, the man is being hanged.

## Features
### Existing Features

+ Name validation
  + It has a function which validates the name, so it includes only letters and in at least 2 characters long
  + It gives different feedbacks depending on the input

![Screenshot of the name validation](media/name-validation.png)

+ Generates a welcome message using the username
  + Asks if the player wants to read the instructions or start the game

![Screenshot of the welcome message](media/welcome-message.png)

+ Validates the input

![Screenshot of the validation](media/validate-input.png)

  + Depending on the input is starts the game, finishes or shows instructions and asks if the player wants to start th game

![Screenshot of instructions](media/show-instructions.png)

+ Random word generation
  + The computer generates a random word
  + The playes sees only "_" and it counts the length of the word
  + It shows a short description of the word to help the player

![Screenshot of the start game](media/start-game.png)

+ Validate input and check the guess
  + If the user guesses wrong it gives a feedback and asks to continue the game

![Screenshot of the wrong guess message](media/check-guess.png)

  + If the user guesses right, it shows a message and if there are more letters to guess, the game continues.

![Screenshot of the right guess](media/check-guess-right.png)

+ Check if the user have already guessed the letter.
  + It shows a message if the user has already guessed the letter, without counting it as a wrong guess.

![Screenshot of the input validation](media/validate-guess.png)

+ The game over function
  + If the man hangs, it shows a message that the game is over and asks if the user wants to play again

![Screenshot of the game over function](media/replay.png)

+ Goodbye message
  + If the user wishes to end the game, it generates a goodbye message

![Screenshot of the goodbye message](media/goodbye.png)

