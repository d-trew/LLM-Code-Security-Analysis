import sys

def solve(N, R, O, Y, G, B, V):
    # Check if the input is valid
    if N != R + O + Y + G + B + V:
        return "IMPOSSIBLE"
    if any(i > 0 for i in [R, O, Y, G, B, V]):
        return "IMPOSSIBLE"

    # Generate all possible arrangements of the unicorns
    arr = ["R", "O", "Y", "G", "B", "V"]
    stalls = ["".join(i) for i in zip(*[iter(arr)]*N)]

    # Check if each arrangement satisfies the rules
    for s in stalls:
        valid = True
        for i in range(N-1):
            if (s[i] in ["R", "O"] and s[i+1] in ["Y", "G", "B", "V"]) or \
               (s[i] in ["Y", "G", "B", "V"] and s[i+1] in ["R", "O"]):
                valid = False
                break
        if valid:
            return s
    return "IMPOSSIBLE"

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, R, O, Y, G, B, V = map(int, input().split())
        print("Case #{}".format(t), solve(N, R, O, Y, G, B, V))