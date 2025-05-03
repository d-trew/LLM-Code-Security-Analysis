import sys

def readline_int_list():
    return list(map(int, input().split()))

t, n, c = readline_int_list()

for _ in range(t):
    print(0)
    sys.stdout.flush()
    a1 = readline_int_list()[0]
    
    if a1 == 0:
        continue
    
    print(n)
    sys.stdout.flush()
    a2 = readline_int_list()[0]
    
    if a2 == 0:
        continue
    
    print((a1 + 1) % n, (a2 + 1) % n)
    sys.stdout.flush()

print(*([0] * t))
sys.stdout.flush()

pens = []
for _ in range(t):
    p1, p2 = readline_int_list()
    pens.append((p1, p2))

succeeded = sum(1 for p1, p2 in pens if p1 != 0 and p2 != 0)
print(succeeded >= c)

sys.exit()