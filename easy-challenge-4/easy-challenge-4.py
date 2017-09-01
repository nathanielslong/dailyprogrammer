from random import randint

def rand_char():
    num = randint(33, 255)
    return chr(num)

def rand_pass(num):
    password = ''
    for i in range(0, int(num)):
        password += rand_char()

def main():
    random = rand_char()
    print(random)

if __name__ == '__main__' : main()
