# My solution treats the title like a base-26 number, eg.AA in base-26 is equal to 27 in out normal base-10 system
def convert_to_title(num):
    # This first part calculates how many letters are needed
    n = 1 
    val = 26
    while val < num:
        n += 1
        val += 26 ** n

    string = ""
    number = num
    for i in range(n - 1,-1,-1): # Works through each digit starting with the foremost and ending with the back one. ie. in the number 229704, it first finds that the first letter is an M, then that the second is an A and so on.
        if number % 26 != 0:
            letter_index = number // (26 ** i)
        else: # This deals with some edge when a Z is involved, I couldn't find a better way of doing it unfortunately
            if number != 26:
                letter_index = (number // (26 ** i)) - 1
            else:
                letter_index = 26
        number = number - letter_index * 26**i
        string += chr(64 + letter_index) # Just using the ASCII system because I think it is easier to implement 

    return string

print(convert_to_title(1))
print(convert_to_title(18))
print(convert_to_title(28))
print(convert_to_title(52))
print(convert_to_title(701))
print(convert_to_title(229704))
print(convert_to_title(209380622941))
# And finally...
print(convert_to_title(105793246561645))
