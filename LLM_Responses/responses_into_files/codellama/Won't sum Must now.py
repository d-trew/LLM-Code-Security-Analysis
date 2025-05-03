import sys

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_minimum_palindromic_terms(target, terms=[]):
    if target == 0:
        return terms
    for i in range(len(str(target))//2+1):
        term = int(str(target)[:i] + str(target)[-i:])
        if is_palindrome(term) and term < target:
            terms.append(term)
            find_minimum_palindromic_terms(target - term, terms)
    return terms

def main():
    test_cases = int(input())
    for i in range(test_cases):
        target = int(input())
        terms = find_minimum_palindromic_terms(target)
        print("Case #{}: {}".format(i+1, " ".join([str(term) for term in terms])))

if __name__ == "__main__":
    main()