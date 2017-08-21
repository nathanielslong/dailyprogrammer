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


# top = 100
# number_range = [1, 100]
# guess = 50

set_range()
print('lower: {}, upper: {}'.format(lower, upper))
