from sys import stdin, setrecursionlimit
setrecursionlimit(10_000)

def max_pancakes(l, r):
    if l == 0 or r == 0:
        return (0, l, r)
    elif l > r:
        return max_pancakes(l - min(l, r), r)
    else:
        return max_pancakes(l, r - min(l, r))

def serve_customers(l, r):
    served = 0
    while l > 0 and r > 0:
        customers_to_serve = min(l, r)
        if customers_to_serve <= l:
            served += customers_to_serve
            l -= customers_to_serve
        else:
            served += l
            l = 0
            r -= l
    return (served, l, r)

for _ in range(int(stdin.readline())):
    l, r = map(int, stdin.readline().split())
    max_pancakes_left, _, _ = max_pancakes(l, r)
    served, remaining_left, remaining_right = serve_customers(max_pancakes_left, min(l, r))
    print(f"Case #{_+1}: {served} {remaining_left} {remaining_right}")