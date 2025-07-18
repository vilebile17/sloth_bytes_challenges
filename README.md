## For a [sloth bytes](https://slothbytes.beehiiv.com/subscribe?ref=vPltYPtWYd) challenge ## 

# What is a valid string? # 
Well, according to the challenge rules, a valid string is one which has the same amount of each character.
For example:
```
"abcde" - valid!
"aabbcc" - invalid!
```
What **also** counts as a valid string, is one which can have **one** character removed to become a string which has the same amount of each character.
For example:
```
"abcdee" - we can remove one "e" to make it "abcde" which means it is valid too!
```
Examples of real words like this include: 'bluebird','murmur','forgiveable' and of course many others that just include unique letters eg. 'cake' 

# What's the extra stuff for? #
I've added some extra files to the repo, in particular read_english_dictionary.py and words_alpha.txt.
Those files come from the repo [english-words](https://github.com/dwyl/english-words) which is a long list of all the words in english (a lot aren't really words) which I used to get some examples of real words which follow the "valid" pattern. Feel free to check out the repo if your interested, it great!
