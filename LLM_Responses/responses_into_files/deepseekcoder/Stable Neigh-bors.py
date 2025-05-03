def solve(R, O, Y, G, B, V):
    colors = "ROYGBV"
    stalls = ["R", "O", "Y", "G", "B", "V"] * 2
    unicorns = [["R", "O"], ["O", "Y"], ["Y", "G"], ["G", "B"], ["B", "V"], ["V", "R"]]
    
    for i in range(len(stalls)):
        if R > 0 and Y > 0:
            stalls[i], stalls[(i+1)%len(stalls)] = stalls[(i+1)%len(stalls)], stalls[i]
            R -= 1
            Y -= 1
    return "IMPOSSIBLE" if any((R, O, Y, G, B, V)) else ''.join(stalls)

T = int(input())
for t in range(1, T+1):
    R, O, Y, G, B, V = 0, 0, 0, 0, 0, 0
    for color in input().split():
        if color == "R": R += 1
        elif color == "O": O += 1
        elif color == "Y": Y += 1
        elif color == "G": G += 1
        elif color == "B": B += 1
        elif color == "V": V += 1
    print("Case #{}: {}".format(t, solve(R, O, Y, G, B, V)))