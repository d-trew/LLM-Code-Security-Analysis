import sys

def incremental_pancakes(L, R):
    served = 0
    while L > 0 and R > 0:
        if L > R:
            pancakes = min(L, R)
            L -= pancakes
            R -= pancakes
        else:
            pancakes = min(L, R)
            R -= pancakes
            L -= pancakes
        served += 1
    return (served, L, R)

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases+1):
        L, R = map(int, input().split())
        result = incremental_pancakes(L, R)
        print("Case #" + str(case) + ": " + str(result[0]) + " " + str(result[1]) + " " + str(result[2]))