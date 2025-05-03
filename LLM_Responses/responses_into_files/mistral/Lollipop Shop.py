import random
from collections import defaultdict

def get_input():
    t = int(input())
    for _ in range(t):
        n, probabilities = map(int, input().split())
        flavors = [0] * n
        for _ in range(n):
            flavors[_] = random.randint(0, 100) / 100
        for _ in range(n):
            d, flavors_liked = map(int, input().split())
            liked_flavors = [i for i in range(n) if flavors[i] <= flavors_liked]
            if not liked_flavors:
                print(-1)
            else:
                sold_flavor = max(liked_flavors, key=lambda x: probabilities[x])
                flavors[sold_flavor] -= 1
                print(sold_flavor)

get_input()


This Python code reads the number of test cases and processes each test case as described. For each test case, it generates a list of probabilities for each flavor (based on the given range), simulates customer preferences using these probabilities, keeps track of which flavors are still available, and sells a lollipop to each customer if possible. If no flavor is liked by the customer or all available flavors have been sold, it prints -1. The code does not output anything after processing all test cases.