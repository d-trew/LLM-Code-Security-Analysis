def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def min_turns():
    N = int(input())
    teacher = tuple(map(int, input().split()))
    kids = [tuple(map(int, input().split())) for _ in range(N-1)]
    
    total_distance = 0
    for person in (teacher,) + kids:
        total_distance += manhattan_distance((0, 0), person)
    
    return total_distance

T = int(input())
for i in range(1, T+1):
    print("Case #{}: {}".format(i, min_turns()))