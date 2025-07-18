from sherlock_valid_strings import is_valid 

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    for word in english_words:
        if is_valid(word) == "YES":
            print(word)
