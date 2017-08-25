import codecs

def main():
    print('Encode or decode via Caesar\'s Cipher!')
    option = input('"e" for encode, "d" for decode: ');
    options = ('e', 'd')
    while option not in options:
        option = input('Not recognized, try again: ')

    if option == 'e':
        text = input('Enter text to encode: ')
        print('Your encoded text is: {}'.format(codecs.encode(text, 'rot13')))
    elif option == 'd':
        text = input('Enter text to decode: ')
        print('Your decoded text is: {}'.format(codecs.decode(text, 'rot13')))

if __name__ == '__main__' : main()
