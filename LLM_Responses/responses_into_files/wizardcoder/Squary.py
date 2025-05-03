import math

def is_squary(lst):
    return sum([x**2 for x in lst]) == sum(lst)**2

def add_elements(lst, k):
    if len(set(lst)) < len(lst):
        lst = list(set(lst))  # remove duplicates to avoid adding the same integer multiple times
    total_sum = sum(lst)
    total_square = math.sqrt(total_sum**2 - sum([x**2 for x in lst])).is_integer() and k >= len(lst)
    if total_square:
        return [int(math.sqrt(total_sum**2 - sum([x**2 for x in lst))] * (len(lst) + 1))] * k
    else:
        return "IMPOSSIBLE"

t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    if is_squary(lst) or len(set(lst)) < len(lst):  # check for squary and remove duplicates
        print("Case #{}: {}".format(i, add_elements(lst, k)) if not is_squary(lst) else "IMPOSSIBLE")
    else:
        print("Case #{}: IMPOSSIBLE".format(i))