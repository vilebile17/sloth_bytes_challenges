def main():
    string =  str(input("What string are ya testin'? :"))
    if string[0] != "#":
        result = False
    elif len(string) != 7:
        result = False
    else:
        result = True
        for char in string[1:]:
            result = result and (char in "0123456789abcdefABCDEF") #This could be considered a bit lazy
    print(result)

main()
