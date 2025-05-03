def main():
    T = int(input())
    for i in range(1, T + 1):
        L, R = map(int, input().split())
        served_customers = 0
        while L >= 1 and R >= 1:
            if L > R:
                L -= 1
                served_customers += 1
            elif R > L:
                R -= 1
                served_customers += 1
            else:
                break
        print("Case #{}: {} {} {}".format(i, served_customers, L, R))<|im_sep|>