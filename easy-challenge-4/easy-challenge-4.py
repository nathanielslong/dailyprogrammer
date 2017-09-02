from random import randint

def rand_char():
    num = randint(33, 127)
    return chr(num)

def rand_pass(num):
    password = ''
    for i in range(0, int(num)):
        password += rand_char()
    return password

def write_pass(passwords):
    with open('passwords.txt', 'w') as f:
        for password in passwords:
            f.write('{}\n'.format(password))

def main():
    num_letters = input('Number of letters in password: ')
    while not num_letters.isdigit():
        num_letters = input('Not valid.\nNumber of letters in password: ')

    num_pass = input('Number of passwords: ')
    while not num_pass.isdigit():
        num_pass = input('Not valid.\nNumber of passwords: ')

    passwords = []
    for x in range(0, int(num_pass)):
        random = rand_pass(num_letters)
        passwords.append(random)

    write_pass(passwords)
    print(passwords)

if __name__ == '__main__' : main()
