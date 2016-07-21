from random import randint


MIN = 0
MAX = 100
mystery_num = randint(MIN, MAX)

def get_min_and_max():
    return MIN, MAX

def get_guess():
    guess = input('Your guess: ')
    try:
        return int(guess)
    except ValueError:
        print('Please enter a number')
        return get_guess()

# Engine to be used by a bot
def api(guess):
    if guess < mystery_num:
        return 'Higher!'
    elif guess > mystery_num:
        return 'Lower!'
    else:
        return 'Yeah! You guessed right!'

def main():
    found = False

    print('Hey! Guess the number')

    while found == False:

        guess = get_guess()

        answer = api(guess)
        print(answer)

        if answer == 'Yeah! You guessed right!':
            found = True


if __name__ == "__main__":
    main()
