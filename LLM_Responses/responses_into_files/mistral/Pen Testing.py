t, n, c = map(int, input().split())
ink_spent = [0] * t
pens_left = list(range(1, n+1))
while True:
    print(' '.join(map(str, pens_left)))
    ink_spent += list(map(int, input().split()))
    if all(i >= 5 for i in sum(zip(*[list(range(i, i+n)) for i in range(n)]), fillvalue=0)):
        break
print(0*t)
pens_taken = []
for i in range(t):
    pens_taken.append(' '.join(map(str, sorted(pens_left))))
    if i < t-1:
        print(0*t)
        for _ in range(t):
            print(0)


Note: This code assumes that the input is a single line containing three integers `T`, `N`, and `C`. The output consists of multiple lines, each containing either one integer or two integers.