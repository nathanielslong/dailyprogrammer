def get_input(name):
    try:
        var = input('Give me a {}: '.format(name))
        return float(var)
    except:
        print('{} must be a number.')
        return get_input(name)


def force():
    mass = get_input('mass')
    accel = get_input('acceleration')
    force = mass * accel
    print('Your force is {}'.format(force))

def mass():
    force = get_input('force')
    accel = get_input('acceleration')
    mass = force / accel
    print('Your mass is {}'.format(mass))

def accel():
    force = get_input('force')
    mass = get_input('mass')
    accel = force / mass
    print('Your acceleration is {}'.format(accel))

def main():
    print('Welcome to the FMA calculator!\nWhat would you like to calculate?')
    print('"f" for force, "m" for mass, "a" for acceleration')
    choice = '-1'
    options = {
            'f' : force,
            'm' : mass,
            'a' : accel
            }
    while choice != 'f' or choice != 'm' or choice != 'a':
        choice = input('Choice: ')
        if choice in options:
            options[choice]()
            break;
        else:
            print('Not a valid option, try again')

if __name__ == '__main__' : main()
