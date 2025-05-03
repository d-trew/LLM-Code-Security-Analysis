def main():
    T = int(input())
    for i in range(1,T+1):
        D = input()
        digits = sorted([int(d) for d in set(D)]
        max_digit = digits[-1] #get the maximum digit
        min_diff = float('inf')
        for j in range(1,max_digit+1):
            for k in range(j+1,max_digit+1):
                first = int("".join([str(d) for d in digits if d>=k])
                second = int("".join([str(d) for d in digits if d<k])
                diff = abs(first-second)
                min_diff = min(min_diff, diff)
        print("Case #{}: {}".format(i, min_diff))