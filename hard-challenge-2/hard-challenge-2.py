# start: press something
# while going, have ability to stop
# lap ability
# write to file
from datetime import datetime

class Stopwatch:
    def __init__(self):
        pass

    def start(self):
        self.start = datetime.now()
        print('Started at {}.'.format(self.start))

    def stop(self):
        total = datetime.now() - self.start
        print('Ended at {}. Total time: {}.'.format(datetime.now(), total))

    def lap(self):
        self.lap_start = datetime.now()
        print('Lap started at {}.'.format(self.lap_start))

    def end_lap(self):
        total = datetime.now() - self.lap_start
        print('Lap ended at {}. Total time: {}.'.format(datetime.now(), total))

def running_choices(stopwatch, lapped = False):
    if not lapped:
        choice = input('"s" to stop, "l" to lap\n')

    else:
        choice = input('"s" to stop completely, "l" to lap again,\
                "e" to end current lap.\n')

    if choice == 's':
        stopwatch.stop()

    elif choice == 'l':
        stopwatch.lap()
        running_choices(stopwatch, True)

    elif choice == 'e' and lapped:
        stopwatch.end_lap()
        running_choices(stopwatch)

    else:
        running_choices(stopwatch)

def main():
    start = input('Stopwatch: "s" to start.\n')
    while start != 's':
        start = input('Stopwatch: "s" to start.\n')

    stopwatch = Stopwatch()
    stopwatch.start()
    running_choices(stopwatch)

if __name__ == '__main__' : main()
