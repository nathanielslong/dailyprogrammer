tokens = {
        '+' : [0, False]
        '-' : [0, False],
        '*' : 1,
        '/' : 1,
        '^' : 2,
        '!' : 3,
        '(' : 9,
        ')' : 0
        }

def get_input(inp = None):
    if inp is None:
        inp = input('Expression: ')
    value = inp.strip().split()
    return value

def shunting(expression):
    number_queue = []
    token_queue = []
    for token in expression:
        if token.isdigit():
            number_queue.append()
        elif token in tokens:


def main():
    print('Hello world')

if __name__ == '__main__' : main()
