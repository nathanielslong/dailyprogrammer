# start: press something
# while going, have ability to stop
# lap ability
# write to file
import datetime

def start():
    start = datetime.datetime.now().time()
    print('Stopwatch started at {}.'.format(start))

def stop():
    end = datetime.datetime.now().time()
    print('this')

def lap():
    print('that')

def main():
    start()
    user_input = input('Stop with "p", lap with "l".\n')
    options = {
            'p' : stop,
            'l' : lap
            }
    while user_input not in options.keys():
        print('Not recognized, try again.')
        user_input = input('Stop with "p", lap with "l".\n')

    options[user_input]()

if __name__ == '__main__' : main()
