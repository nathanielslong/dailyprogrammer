events = {}

def list_events():
    print('Events:\n-----------------')
    if len(events.keys()) == 0:
        print('No events entered.')

    else:
        for hour in sorted(events.keys()):
            print('Hour: {}, description: {}'.format(hour, events[hour]))

    print()

def valid_hour(hour):
    if not hour.isdigit():
        print('Not a positive numeric value, try again.')
        return False

    elif int(hour) < 0 or int(hour) > 23:
        print('Not a valid hour, try again.')
        return False

    else:
        return True

def get_hour():
    hour = input('Hour of event: ')
    while not valid_hour(hour):
        hour = input('Hour of event: ')

    return int(hour)

def add_event():
    hour = get_hour()
    if int(hour) in events:
        print('Hour already taken.\n')
        return

    description = input('Description of event: ')
    events[hour] = description
    print('Event added.\n')

def edit_event():
    hour = get_hour()
    if int(hour) not in events:
        print('Hour not assigned, cannot edit.\n')
        return

    description = input('New description of event: ')
    events[hour] = description
    print('Event edited.\n')

def remove_event():
    hour = get_hour()
    if int(hour) not in events:
        print('Hour not assigned, cannot delete.\n')
        return

    choice = input('Are you sure? (y, n): ')
    choices = ('y', 'n')
    while choice not in choices:
        print('Not a valid choice, try again.')
        choice = input('Are you sure? (y, n): ')

    if choice == choices[0]:
        del events[hour]
        print('Event deleted.\n')

    elif choice == choices[1]:
        print('Event not deleted.')

def quit():
    return
# fill in

def main():
    print('Welcome to the hourly event planner!')

    options = {
            'a' : ('Add event', add_event),
            'e' : ('Edit event', edit_event),
            'l' : ('List events', list_events),
            'r' : ('Remove event', remove_event),
            'q' : ('Quit', quit)
            }
    choice = '-1'

    while choice != 'q':
        print('Options \n----------------')
        for key, option in options.items():
            print('{}, {}'.format(key, option[0]))

        choice = input('Enter an option: ')
        if choice in options:
            options[choice][1]()
        else:
            print('Error: not an option, please try again.')

if __name__ == '__main__' : main()
