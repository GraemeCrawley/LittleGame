import main
import time

from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Bot():
    """
    Text-based version of the bot class, which acts as the facilitator of the game.
    @type MAX: integer
    @param MAX: The default maximum guess
    @type MIN: integer
    @param MIN: The default minimum guess
    """
    MAX = 100
    MIN = 0

    def __init__(self, name):
        self.name = name

    def welcome(self):
        """
        Welcomes the player to the game. Prints the name of the bot and the game.
        """
        print('Hello! My name is {0} and I can play guessing game'.format(
            self.name))
        # Get game area from engine
        self.MIN, self.MAX = main.get_min_and_max()
        print('Retrieved game area {0}, {1}'.format(self.MIN, self.MAX))

    def play(self):
        """
        Allows the bot to play the game with the human player

        @type max_guess: integer
        @param max_guess: holds the current max guess
        @type min_guess: integer
        @param min_guess: holds the current min guess
        @type guess_index: integer
        @param guess_index: holds the current number of guesses made
        @type answer: string
        @param answer: hold the bots answer to the guess
        """
        max_guess = self.MAX
        min_guess = self.MIN
        guess_index = 0
        answer = ''

        #While loop to run if they haven't guessed right
        while answer != 'Yeah! You guessed right!':
            guess_index += 1
            time.sleep(0.5)

            #Logic to change the max and min guess
            if answer == 'Lower!':
                max_guess = guess
            elif answer == 'Higher!':
                min_guess = guess

            #Calculate next guess
            guess = int((max_guess - min_guess) / 2) + min_guess
            print('{0}. Bot: Let\'s try {1}'.format(guess_index, guess))
            answer = main.api(guess)

        print('Bot: I have won!')


class UIBot(Widget):
    """
        Graphical version of the bot class, which acts as the facilitator of the game.

        @type name: string
        @param name: The name of the bot
        @type MAX: integer
        @param MAX: maximum value of the guess
        @type MIN: integer
        @param MIN: minimum value of the guess    
        @type messages: string
        @param messages: message to be printed to the screen
        """
    name = 'John'
    messages = StringProperty('yaa\n')
    MAX = 100
    MIN = 0


    def welcome(self):
        """
        Welcomes the player to the game. Prints the name of the bot and the game.
        """
        self.write_msg('Hello! My name is {0} and I can play guessing game'.format(
            self.name))
        # Get game area from engine
        self.MIN, self.MAX = main.get_min_and_max()
        self.write_msg('Retrieved game area {0}, {1}'.format(self.MIN, self.MAX))

    def play(self):
          """
        Allows the bot to play the game with the human player

        @type max_guess: integer
        @param max_guess: holds the current max guess
        @type min_guess: integer
        @param min_guess: holds the current min guess
        @type guess_index: integer
        @param guess_index: holds the current number of guesses made
        @type answer: string
        @param answer: hold the bots answer to the guess
        """
        max_guess = self.MAX
        min_guess = self.MIN
        guess_index = 0
        answer = ''


        #While loop to run if they haven't guessed right
        while answer != 'Yeah! You guessed right!':
            guess_index += 1
            time.sleep(0.5)

            #Logic to change the max and min guess
            if answer == 'Lower!':
                max_guess = guess
            elif answer == 'Higher!':
                min_guess = guess

            #Calculate next guess
            guess = int((max_guess - min_guess) / 2) + min_guess
            self.write_msg('{0}. Bot: Let\'s try {1}'.format(guess_index, guess))
            answer = main.api(guess)

        self.write_msg('Bot: I have won!')

    #Starts the bot up
    def start_bot(self):
        self.welcome()
        self.play()

    #Allows the bot to ouput messages
    def write_msg(self, msg):
        self.messages += msg + '\n'


if __name__ == "__main__":
    robot = Bot('John')
    robot.welcome()
    robot.play()
