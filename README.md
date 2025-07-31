## For all of the [sloth bytes](https://slothbytes.beehiiv.com/subscribe?ref=vPltYPtWYd) challenge solutions that I've made ## 

# Sherlock Valid Strings #
### what is a valid string? ###
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


# Word Overlapping #
Given two words, it combines them in a way which makes their letters overlap. For example:
```
"hippopotamus" + "mustard" -> "hippopotamustard"
"sugar" + "sugar" -> "sugar"
```
And if it's impossible to merge them...
```
"water" + "bottle" -> "waterbottle"
```



