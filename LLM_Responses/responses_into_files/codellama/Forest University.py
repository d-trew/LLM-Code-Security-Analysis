# Write a Python program based on this description.
# Return ONLY the Python code with no additional explanation or formatting.

Case #1: y1=1, y2=1, y3=0, y4=0, y5=0
Case #2: y1=2, y2=0, y3=1, y4=0, y5=1

# Write a Python program based on this description.
# Return ONLY the Python code with no additional explanation or formatting.

import math

def fraction_of_valid_sequences(cool_words):
    number_of_sequences = 0
    for cool_word in cool_words:
        if cool_word in "CJ":
            number_of_sequences += 1
    return number_of_sequences / len(cool_words)

def main():
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print("Case #" + str(case) + ":", end=" ")
        cool_words = input().split()
        y = fraction_of_valid_sequences(cool_words)
        print(y)

if __name__ == "__main__":
    main()