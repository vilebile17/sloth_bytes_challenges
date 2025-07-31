def make_dictionary(string):
    # this turns the strng into a dictionary containing character to count mapping
    cool_dict = {}
    for char in string:
        if char in cool_dict:
            cool_dict[char] += 1
        else:
            cool_dict[char] = 1
    return cool_dict


def find_max(cool_dict):
    max_so_far = float("-inf")
    for key in cool_dict:
        if cool_dict[key] > max_so_far:
            max_so_far = cool_dict[key]
            gigachad_key = key
    return gigachad_key


def all_the_same(cool_dict):
    # figures out if all of the characters have the same frequency
    values = list(cool_dict.values())
    for value in values:
        if value != values[0]:
            # According to Euclid: 'magnitudes which are equal to the same are equal to each other'
            return False 
    return True


def is_valid(string):
    cool_dict = make_dictionary(string)
    # first check if all of the characters appear the same number of times
    if all_the_same(cool_dict):
        return "YES"
    # if not we find the most frequent character and then subtract one from it's count and then try again
    most_frequent_char = find_max(cool_dict)
    cool_dict[most_frequent_char] -= 1
    if all_the_same(cool_dict):
        return "YES"
    return "NO"


def main():
    print("===== WELCOME, MY FRIEND =====")
    cool_string = str(input("What is the string you want to test? : "))
    print("...")
    print(f"Is it valid? {is_valid(cool_string)}!")


main()
