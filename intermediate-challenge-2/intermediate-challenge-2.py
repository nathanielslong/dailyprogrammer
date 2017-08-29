state = 0
space = [0, 0]

def get_direction():
    directions = {
            'n' : 'North',
            's' : 'South',
            'e' : 'East',
            'w' : 'West'
            }

    direction = input('What direction shall you go?\n')
    while direction not in directions.keys():
        print('That\'s not a direction! Try again!')
        direction = input('What direction shall you go?\n')

    print('{} it is!'.format(directions[direction]))
    return direction

def move_to_space(direction):
    spaces = {
            'n' : [1, 0],
            's' : [-1, 0],
            'e' : [0, 1],
            'w' : [0, -1]
            }

    for keys in spaces:
        if direction in keys:
            x1 = space[0]
            y1 = space[1]

            x2 = spaces[direction][0]
            y2 = spaces[direction][1]

            space[0] = x1 + x2
            space[1] = y1 + y2

    print(space)

def space_effect():
    return

def main():
    username = input('What is your name?\n')
    print('Hello, {}.'.format(username))

    while state == 0:
        direction = get_direction()
        move_to_space(direction)
        space_effect()

if __name__ == '__main__' : main()
