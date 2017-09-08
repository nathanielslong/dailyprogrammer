from random import randint

class Crypt():
    def __init__(self, number):
        self.__cipher = []
        self.__make_cipher(number)

    def __make_cipher(self, number):
        for x in range(0, number):
            self.__cipher.append(randint(32, 126))

    def encrypt(self, phrase, is_encrypt):
        count = 0
        length = len(self.__cipher)
        new_phrase = []

        for char in phrase:
            if count == length:
                count = 0

            if is_encrypt:
                new_char = chr((ord(char) + self.__cipher[count]) % 126)
            else:
                new_char = chr((ord(char) - self.__cipher[count]) % 126)

            new_phrase.append(new_char)
            count += 1

        return ''.join(new_phrase)

def get_int(phrase):
    val = input(phrase)
    while not val.isdigit():
        print('Not a positive integer, try again.')
        val = input(phrase)
    return abs(int(val))

def main():
    phrase = input('Phrase to be encrypted: ')
    cipher_size = get_int('Size of cipher: ')

    crypt = Crypt(cipher_size)
    encrypted = crypt.encrypt(phrase, True)
    print(encrypted)

    decrypted = crypt.encrypt(encrypted, False)
    print(decrypted)

if __name__ == '__main__' : main()
