def longest_straight(n, sides):
    count = [0] * (max(sides) + 2)
    for side in sides:
        count[side] += 1
    
    max_length = 0
    current_length = 0
    for i in range(1, len(count)):
        if count[i]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    
    return max_length

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    sides = list(map(int, input().split()))
    print("Case #{}: {}".format(i, longest_straight(n, sides)))