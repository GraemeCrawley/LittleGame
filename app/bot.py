import main
import time

from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class Bot():
    MAX = 100
    MIN = 0

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print('Hello! My name is {0} and I can play guessing game'.format(
            self.name))
        # Get game area from engine
        self.MIN, self.MAX = main.get_min_and_max()
        print('Retrieved game area {0}, {1}'.format(self.MIN, self.MAX))

    def play(self):
        max_guess = self.MAX
        min_guess = self.MIN
        guess_index = 0
        answer = ''

        while answer != 'Yeah! You guessed right!':
            guess_index += 1
            time.sleep(0.5)

            if answer == 'Lower!':
                max_guess = guess
            elif answer == 'Higher!':
                min_guess = guess

            guess = int((max_guess - min_guess) / 2) + min_guess
            print('{0}. Bot: Let\'s try {1}'.format(guess_index, guess))
            answer = main.api(guess)

        print('Bot: I have won!')


class UIBot(Widget):
    name = 'John'
    messages = StringProperty('yaa\n')
    MAX = 100
    MIN = 0


    def welcome(self):
        self.write_msg('Hello! My name is {0} and I can play guessing game'.format(
            self.name))
        # Get game area from engine
        self.MIN, self.MAX = main.get_min_and_max()
        self.write_msg('Retrieved game area {0}, {1}'.format(self.MIN, self.MAX))

    def play(self):
        max_guess = self.MAX
        min_guess = self.MIN
        guess_index = 0
        answer = ''

        while answer != 'Yeah! You guessed right!':
            guess_index += 1
            time.sleep(0.5)

            if answer == 'Lower!':
                max_guess = guess
            elif answer == 'Higher!':
                min_guess = guess

            guess = int((max_guess - min_guess) / 2) + min_guess
            self.write_msg('{0}. Bot: Let\'s try {1}'.format(guess_index, guess))
            answer = main.api(guess)

        self.write_msg('Bot: I have won!')

    def start_bot(self):
        self.welcome()
        self.play()

    def write_msg(self, msg):
        self.messages += msg + '\n'


if __name__ == "__main__":
    robot = Bot('John')
    robot.welcome()
    robot.play()
