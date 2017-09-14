text_file = open('anagrams.txt').read().split()

def main():
    sorted_text = [''.join(sorted(word)) for word in text_file]
    anagrams = [word for word in sorted_text if sorted_text.count(word) > 1]
    count = len(anagrams)
    print('Anagrams in file: {}.\nNumber of total anagrams: {}'.format(anagrams, count))

if __name__ == '__main__' : main()
