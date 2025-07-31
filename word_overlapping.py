import sys

def overlap(word_one, word_two):
    for i in range(len(word_one),0,-1):
        if word_one[-i:] == word_two[:i]:
            return word_one + word_two[i:]
    return word_one + word_two

if len(sys.argv) == 3:
    print(overlap(sys.argv[1],sys.argv[2]))
else:
    print("USAGE: python3 word_overlapping.py <word_one> <word_two>")
