import string

def get_digit(word):
    return {'ZERO': '0', 'ONE': '1', 'TWO': '2', 'THREE': '3', 'FOUR': '4', 'FIVE': '5', 'SIX': '6', 'SEVEN': '7', 'EIGHT': '8', 'NINE': '9'}[word]

def main():
    T = int(input())
    for i in range(1, T + 1):
        S = input()
        digits = []
        for word in string.ascii_uppercase:
            if word in S:
                digit = get_digit(word)
                while word in S and len(digits) < 10:
                    index = S.index(word)
                    digits.append(digit)
                    S = S[:index] + S[index+len(word):]
        print("Case #{}: {}".format(i, ''.join(sorted(digits)))

if __name__ == "__main__":
    main()