import sys

def min_copyright_cost(x, y, s):
    cost = 0
    for i in range(len(s) - 1):
        if s[i] == '?' and (s[i:i+2] == "CJ" or s[i:i+2] == "JC"):
            if s[i+1] == '?':
                cost += x + y
            else:
                cost += min(x, y)
    return cost

def main():
    test_cases = int(input())
    for i in range(test_cases):
        x, y, s = map(int, input().split())
        print("Case #%d: %d" % (i+1, min_copyright_cost(x, y, s)) 

if __name__ == "__main__":
    main()