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
        while True:
            if self.start_game == "S":
                pass
            elif self.start_game == "I":
                pass
            elif self.start_game == "E":
                pass
            else:
                self.start_guess = input("Please enter a valid value: \n").upper()





user1 = Hangman(name = "asya")
user1.welcome()



