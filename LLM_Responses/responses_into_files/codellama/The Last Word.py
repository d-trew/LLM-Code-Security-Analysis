import sys

def last_word(string):
    # sort the string alphabetically
    sorted_string = sorted(string)
    # initialize a variable to keep track of the last word
    last_word = ""
    for letter in sorted_string:
        # if the letter is not already in the last word, add it to the end
        if letter not in last_word:
            last_word += letter
        # otherwise, add it to the beginning of the word
        else:
            last_word = letter + last_word
    return last_word

# read the number of test cases
T = int(sys.stdin.readline())

# loop through each test case
for i in range(1, T+1):
    # read the string from standard input
    string = sys.stdin.readline().strip()
    # find the winning last word and print it to standard output
    print("Case #{}: {}".format(i, last_word(string)))