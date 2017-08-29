# start: press something
# while going, have ability to stop
# lap ability
# write to file
import datetime


lap = 0

def start():
    start = datetime.datetime.now()
    print('Stopwatch started at {}.'.format(start))
    return start

def stop(start):
    end = datetime.datetime.now()
    total = end - start
    print('Time ended, total time: {}'.format(total))

def lap():
    print('that')

def main():
        start_time = start()
        options = {
                'p' : stop,
                'l' : lap
                }
        user_input = input('Stop with "p", lap with "l".\n')
        while user_input not in options.keys():
            print('Not recognized, try again.')
            user_input = input('Stop with "p", lap with "l".\n')

        options[user_input](start_time)

if __name__ == '__main__' : main()
