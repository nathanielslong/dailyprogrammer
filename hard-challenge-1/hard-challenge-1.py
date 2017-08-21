lower = 0
upper = 100

def set_lower():
    print('Please give a lower bound.')
    lower_str = input('Lower bound: ')
    while not lower_str.isdigit():
        print('Lower bound must be a positive integer.')
        lower_str = input('Lower bound: ')
    global lower
    lower = int(lower_str)

def set_upper():
    print('Please give an upper bound.')
    upper_str = input('Upper bound: ')
    while not upper_str.isdigit():
        print('Upper bound must be a positive integer.')
        upper_str = input('Upper bound: ')
    global upper
    upper = int(upper_str)

def set_range():
    set_lower()
    set_upper()
    if upper == lower:
        print('Values must be different for a range, please try again.')
        set_range()
    elif upper < lower:
        print('Upper bound must be larger than the lower.')
        set_upper()

def guess_correct(guess):
    print('{} is the guess, is that correct?'.format(guess))
    check = input('"y" if correct, "l" if too low, "h" if too high: ')
    while check != 'y' or check != 'l' or check != 'h':
        print('That\'s not a recognized command, try again.')
        check = input('"y" if correct, "l" if too low, "h" if too high: ')
    return check

def set_value(answer, guess):
    if answer == 'l':
        global lower
        lower = guess

    if answer == 'h':
        global upper
        upper = guess

def main():
    print('Guessing game: For ranges 1 to very large numbers.\n----------------')
    set_range()
    print('Lower bound: {}, Upper bound: {}'.format(lower, upper))
    answer = 'n'
    while answer != 'y':
        print('Current range: {}, {}'.format(lower, upper))
        guess = int((upper + lower) / 2)
        answer = guess_correct(guess)
        set_value(answer, guess)
    print('Your number was {}.'.format(guess))


if __name__ == '__main__' : main()
