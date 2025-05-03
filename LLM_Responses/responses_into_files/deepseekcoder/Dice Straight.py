Here is the Python code for your problem:


import bisect
from collections import defaultdict

def longest_straight(dice):
    sorted_faces = [sorted([face[i] for face in dice]) for i in range(6)]
    dp, ends = [], []
    for faces in zip(*sorted_faces):
        idx1 = bisect.bisect_left(dp, (faces[0],))
        if len(dp) == idx1:
            dp.append((faces[0], 1))
        else:
            dp[idx1] = (faces[0], max(ends[idx1][1]+1, dp[idx1][1]))
        idx2 = bisect.bisect_left(ends, (faces[-1],), key=lambda x:x[0])
        if len(ends) == idx2:
            ends.append((faces[-1], max(dp[-1][1]+1, 1)))
        else:
            ends[idx2] = (faces[-1], dp[-1][1])
    return dp[-1][1] if dp[-1][0] == sorted_faces[0][-1] else max(dp[-1][1], ends[-1][1])

def main():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        dice = [list(map(int, input().split())) for _ in range(n)]
        print("Case #{}: {}".format(i+1, longest_straight(dice)))

if __name__ == "__main__":
    main()

This program uses dynamic programming to solve the problem. It sorts each die's faces and maintains two lists (dp and ends) for processing all dice one by one from left to right. dp[i] represents the longest straight ending with the i-th face, while ends[i] represents the longest straight starting with the i-th face.