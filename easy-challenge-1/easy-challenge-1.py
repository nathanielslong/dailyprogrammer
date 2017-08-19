person = input('Enter your name: ')
age = input('Enter your age: ')
username = input('Enter your reddit username: ')

print('your name is {}, you are {} years old, and your username is {}'.format(person, age, username))

file = open('names.txt', 'a')
file.write('{}, {}, {}\n'.format(person, age, username))
file.close()
