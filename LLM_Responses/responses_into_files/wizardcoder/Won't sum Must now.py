import sys
sys.setrecursionlimit(10**6)
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_minimum_terms(s, terms=[]):
    if s < 1:
        return terms
    for i in range(10**len(str(s)), 10**(len(str(s)-1), -1, -1):
        if is_palindrome(i) and i <= s:
            new_terms = find_minimum_terms(s-i, terms+[i])
            if sum(new_terms) == s:
                return new_terms
    return []

def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        s = int(input())
        terms = find_minimum_terms(s)
        if len(terms) == 1:
            print("Case #{}: {}".format(case, terms[0])
        elif len(terms) == 2:
            print("Case #{}: {} {}".format(case, terms[0], terms[1])
        else:
            print("Case #{}: {} {} {}".format(case, terms[0], terms[1], terms[2])

if __name__ == "__main__":
    main()