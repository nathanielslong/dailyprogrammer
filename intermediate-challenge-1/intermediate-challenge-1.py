# events calendar-ish
# can CRUD
# no events hardcoded
# each event will have the following:
#   a title
#   a date

events = {}

def list_events():
    print('Events listed:\n\n\n')
# fill in

def add_event():
    print('Add event:\n\n\n')
# fill in

def remove_event():
    print('Remove event:\n\n\n')
# fill in

def update_event():
    print('Update event:\n\n\n')
# fill in

def quit():
    return
# fill in

def main():
    print('Welcome to the event planner!')

    options = {
            'l' : ('List events', list_events),
            'a' : ('Add event', add_event),
            'r' : ('Remove event', remove_event),
            'u' : ('Update event', update_event),
            'q' : ('Quit', quit)
            }
    choice = '-1'

    while choice != 'q':
        print('Options \n ----------------')
        for key, option in options.items():
            print('{}, {}'.format(key, option[0]))

        choice = input('Enter an option: ')
        if choice in options:
            options[choice][1]()
        else:
            print('Error: not an option, please try again.')

if __name__ == '__main__' : main()
