import sys

def get_edit_distance(str1, str2):
    d = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j - 1] + 1, d[i - 1][j] + 1, d[i][j - 1] + 1)
    return d[-1][-1]

def find_compromise(str1, str2):
    compromise = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            compromise += str1[i]
        else:
            compromise += str2[i]
    return compromise

def main():
    t = int(input())
    for _ in range(t):
        c, j = input().split()
        cd = get_edit_distance(c, j)
        jd = get_edit_distance(j, c)
        if abs(cd - jd) < 2:
            compromise = find_compromise(c, j)
            print("Case #{}: {}".format(_ + 1, compromise))
        else:
            print("Case #{}: {}".format(_ + 1, c if cd < jd else j))

if __name__ == "__main__":
    main()