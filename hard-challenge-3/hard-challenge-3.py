word_list = open('text-list.txt').read().split()

scrambled_words = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle',
                   'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

def main():
    for scrambled in sorted(scrambled_words, key=len):
        matches = [word for word in word_list if sorted(scrambled) == sorted(word)]
        print('{}: '.format(scrambled).join(matches))

if __name__ == '__main__' : main()
