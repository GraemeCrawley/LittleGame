from random import randint

"""
    @type MAX: integer
    @param MAX: The default maximum guess
    @type MIN: integer
    @param MIN: The default minimum guess
    @type mystery_num: integer
    @param mystery_num: creates a random integer to guess
"""
MIN = 0
MAX = 100
mystery_num = randint(MIN, MAX)


def get_min_and_max():
    """
    Gets the mamimum and minimum values currently guessed.
    @rtype: integer
    @return: he maximum and minum guesses made up to the time called
    """
    return MIN, MAX

def get_guess():
    """
    Gets the guess from the input.
    @type guess: integer
    @param guess: the guess made by the user
    @rtype: integer
    @return: the guess made by the user
    """
    guess = input('Your guess: ')
    try:
        return int(guess)
    except ValueError:
        print('Please enter a number')
        return get_guess()

# Engine to be used by a bot
def api(guess):
    """
    Checks if the guess is higher or lower than value they are guessing at.
    @rtype: string
    @return: the outcome of the guess
    """
    #Logic to see if thhe guess is higher, lower, or correct
    if guess < mystery_num:
        return 'Higher!'
    elif guess > mystery_num:
        return 'Lower!'
    else:
        return 'Yeah! You guessed right!'

def main():
    """
    Runs the guessing game for a single user.
    @type found: boolean
    @param found: tracks whether the number has been guessed
    @type guess: integer
    @param guess: the guess that the user has made
    @type answer: string
    @param answer: the outcome of the guess made by the user
    """
    found = False

    print('Hey! Guess the number')

    #Game runs while the number to be guessed has not be found
    while found == False:
        guess = get_guess()
        answer = api(guess)
        print(answer)

        #Prints when the answer is guessed correctly
        if answer == 'Yeah! You guessed right!':
            found = True

if __name__ == "__main__":
    main()
