import hashlib
import os.path

def dict_from_file():
    credentials = open('credentials.txt', 'r').read().split('\n')
    cred_dict = {}

    for row in credentials:
        formatted_row = row.split(',')
        cred_dict[formatted_row[0]] = formatted_row[-1]

    del(cred_dict[''])
    return cred_dict

def check_credentials(username, password):
    if not os.path.isfile('credentials.txt'):
        print('No valid users.')
        return False

    credentials = dict_from_file()

    for user, pass_val in credentials.items():
        if user == username and pass_val == password:
            return True
    return False

def main():
    username = input('Welcome to the top secret program.\nUsername: ')
    password = input('Password: ')
    if check_credentials(username, password):
        print('Welcome to the program, {}.'.format(username))
    else:
        print('ABORT ABORT ABORT')

if __name__ == '__main__' : main()
