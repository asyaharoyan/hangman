# import random to shuffle the words
import random

class Hangman:
    words = {
    "PYTHON": "A powerful programming language",
    "HANGMAN": "A classic word-guessing game",
    "DEVELOPER": "Someone who writes code",
    "PROGRAMMING": "The process of writing computer programs",
    "COMPUTER": "An electronic device for processing data",
    "SOFTWARE": "Programs and data that run on a computer",
    "CODING": "The act of writing code or programming",
    "ALGORITHM": "A step-by-step procedure for solving a problem",
    "FUNCTION": "A reusable block of code that performs a specific task",
    "VARIABLE": "A storage location identified by a memory address and a symbolic name",
    "DEBUGGING": "The process of finding and fixing errors in code",
    "SYNTAX": "The set of rules that dictate the combinations of symbols that are considered to be correctly structured programs",
    "FRAMEWORK": "A pre-built structure that developers can use to build software applications",
    "DATABASE": "A structured collection of data",
    "KEYBOARD": "An input device that uses a set of keys or buttons to send data to a computer",
    "ITERATION": "The repetition of a process in order to generate a sequence of outcomes",
    "RECURSION": "A programming concept where a function calls itself directly or indirectly",
    "INTERFACE": "A point where two systems meet and interact",
    "CONDITION": "A statement that controls the flow of execution in a program",
    "STATEMENT": "An instruction that performs an action in a program",
    "LOOP": "A programming construct that repeats a group of statements",
    "CLASS": "A blueprint for creating objects",
    "OBJECT": "An instance of a class in object-oriented programming",
    "METHOD": "A function associated with an object in object-oriented programming"
}

    # the hangman picture
    hangman = [
    """
   ______________
   |_______
   |      |
   |      
   |     
   |     
   _____________
    """, 
    """
   ______________
   |_______
   |      |
   |      O
   |     
   |     
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |      |
   |     
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |     /|
   |      
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     
   _____________
   """, 
   """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     / 
   _____________
   """, """
   ______________
   |_______
   |      |
   |      O
   |     /|\\
   |     / \\
   _____________
   """
   ]

    def __init__(self, name):
       self.name = name
       self.start_game = None
       self.start_guess = None
       self.word = ""
       self.current_guess = ""
       self.description = ""
       self.used_letters = []

    def show_instructions(self):
        """
        Shows the instructions of the game and asks if the player wants to play.
        """
        print("""
        The computer is going to choose a random word. 
        You need to guess the letter. 
        You have 6 chances to fail. 
        You can not guess the same letter 2 times. 
        If you do not guess the word, the man will be hanged :(
        --------------------------------------------------------
        """)
        self.start_guess = input("Do you want to start the game? (Y/N)\n").upper()
        
        return self.start_guess

    def random_word(self):
        """
        The function chooses a random word from the list and its description.
        """
        self.word = random.choice(list(Hangman.words.keys()))
        self.current_guess = "_ " * len(self.word)
        self.description = Hangman.words[self.word]
        return self.current_guess, self.description

    def check_guess(self):
        """
        The function checks if the player guessed right and adds the letter in the word. 
        If it is a wrong guess or the player guesses the same letter the function informs the player 
        and gives a chance to guess again.
        """
        self.random_word()
        print(self.description)
        # local variable to keep track on wrong answers
        wrong = 0
        # Loop the function untill the game is over.
        while wrong < len(self.hangman) - 1 and "_" in self.current_guess:
            print(self.hangman[wrong])
            print("You have used the following letters: ", self.used_letters,
               "\n")
            print("The word is ", self.current_guess, "\n")
            guess = input("Please guess a letter:  ").upper()

            # check if the input is a letter. 
            # The line of the code is taken from https://codereview.stackexchange.com/
            if not guess.isalpha():
                print("That is not a letter. Please try again! \n")
                pass
            elif len(guess) > 1:
                print("Please pick one letter!")
                continue

            # check if the user has already guessed the letter
            if guess in self.used_letters:
                print("""
            _______________________________________________________
            You've already guessed that letter. Try a different one.
            -------------------------------------------------------
            """)
                continue

            if guess in self.word:
                # using enumerate method to find the right letter on the right index
                for word_index, guess_word in enumerate(self.word):
                    if guess_word == guess:
                        for letter in self.current_guess:
                            self.current_guess = (self.current_guess[:word_index * 2] + 
                            guess_word +self.current_guess[word_index * 2 + 1:])

                #Congradulate the player and continue the game            
                print("Correct guess! ", self.current_guess, "\n")
                self.used_letters.append(guess)
            else:
                self.used_letters.append(guess)
                wrong += 1
                print("Unfortunately you guessed wrong. Pick another letter! \n")
                continue

        #checking if there are no _, then the player guessed the word
        if "_" not in self.current_guess:
            print(
             """
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             Congratulations! You guessed the word:
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             """, self.word, "\n")
            self.restart_hangman()
        else:
            print(self.hangman[wrong])
            print("You could not guess the word. The game is over.\n")
            print("The word was ", self.word, "\n")
            self.restart_hangman()

    def welcome(self):
        """
        The start of the game. Welcomes the player and asks if they want to read instryctions.
        """
        print(f"""
        ******************************
        Welcome to HANGMAN {self.name}.
        ******************************
        ------------------------------
        """)
        self.start_game = input("""
        ///////////////////////////////////////////////////////////////////
        Do you want to read the instuctions or you want to start the game?
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        -------------------------------------------------------------------\n
        Tye:
        S to START the game,
        E to EXIT the game,
        I to read the INSTRUCTIONS: \n
        """).upper()
        self.check_welcome_input()
        return self.start_game

    def check_welcome_input(self):
        """
        The function checks and validates the user input to call functions accordingly.
        """
        while True:
            if self.start_game == "S":
                self.check_guess()
            elif self.start_game == "I":
                pass
            elif self.start_game == "E":
                pass
            else:
                self.start_guess = input("Please enter a valid value: \n").upper()





user1 = Hangman(name = "asya")
user1.welcome()



