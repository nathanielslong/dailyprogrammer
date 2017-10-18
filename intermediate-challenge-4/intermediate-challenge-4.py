tokens = {
        '+' : [0, False]
        '-' : [0, False],
        '*' : [1, False],
        '/' : [1, False],
        '^' : [2, False],
        '!' : [3, False],
        '(' : [9, True],
        ')' : [0, True]
        }

def get_input(inp = None):
    if inp is None:
        inp = input('Expression: ')
    value = inp.strip().split()
    return value

def shunting(expression):
    output_queue = []
    token_queue = []
    for token in expression:
        if token.isdigit():
            output_queue.append()
        elif token in tokens:
            if token[1] != true:

def main():
    print('Hello world')

if __name__ == '__main__' : main()
