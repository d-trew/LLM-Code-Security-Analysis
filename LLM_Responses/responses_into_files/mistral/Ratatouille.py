import sys
from itertools import product

def check_kit(serving_req, ingredient_packages):
    for package in ingredient_packages:
        if (package[0] / serving_req[0] < 0.9 or serving_req[0] / package[0] > 1.1) \
                or (package[1] / serving_req[1] < 0.9 or serving_req[1] / package[1] > 1.1):
            return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        N, *ingredient_packages = list(map(int, input().split()))
        ingredients = sorted(ingredient_packages)
        max_servings = 0
        for servings in range(1, min(N + 1, len(ingredients))):
            serving_req = [sum([x // N for x in ingredients[:servings]], 0), sum([x // N for x in ingredients[servings:]])]
            if check_kit(serving_req, ingredients):
                max_servings = max(max_servings, servings)
        print(f'Case #{_+1}: {max_servings}')

if __name__ == '__main__':
    main()


This Python code reads the number of test cases from the standard input and then iterates through each test case. For each test case, it first reads the number of ingredients and their respective package sizes. It sorts the ingredients in ascending order and initializes a variable `max_servings` to 0.

Next, it iterates through all possible numbers of servings from 1 up to the minimum of the number of ingredients or the total number of servings required for one full serving (N). For each potential number of servings, it calculates the required amount of each ingredient for that number of servings and checks if the packages have enough of each ingredient within the allowed range. If they do, it updates `max_servings` to be the maximum of its current value and the potential number of servings.

Finally, it prints the result for the current test case as 'Case #x: y', where x is the test case number and y is the maximum number of kits that can be formed.