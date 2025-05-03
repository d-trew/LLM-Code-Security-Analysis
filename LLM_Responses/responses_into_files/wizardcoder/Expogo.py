import sys

def expogo_stick(x, y):
    if x == 0 and y == 0:
        return "IMPOSSIBLE"
    n = abs(x) + abs(y)
    jumps = ""
    current_x = 0
    current_y = 0
    for i in range(1, n+1):
        if x > y:
            if current_x < x and current_y == y:
                jumps += "E" * (i*2 - 1) + "N" * (i-1)
                current_x = i * i
                current_y = 0
        elif x < y:
            if current_x == x and current_y < y:
                jumps += "S" * (i*2 - 1) + "W" * (i-1)
                current_x = 0
                current_y = i * i
        elif x > 0:
            if current_x < x and current_y == y:
                jumps += "E" * (i*2 - 1) + "N" * (i-1)
                current_x = i * i
                current_y = 0
        elif x < 0:
            if current_x > x and current_y == y:
                jumps += "W" * (i*2 - 1) + "S" * (i-1)
                current_x = -i * i
                current_y = 0
        elif y < 0:
            if current_y > y and current_x == x:
                jumps += "N" * (i*2 - 1) + "E" * (i-1)
                current_y = -i * i
                current_x = 0
        elif y > 0:
            if current_y < y and current_x == x:
                jumps += "S" * (i*2 - 1) + "W" * (i-1)
                current_y = i * i
    return jumps

inputs = int(sys.stdin.readline())
for i in range(1, inputs+1):
    x, y = map(int, input().split())
    print("Case #{}: {}".format(i, expogo_stick(x, y))