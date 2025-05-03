import sys
input = sys.stdin.readline
def process(s):
    highlighted_chars = []
    for i in range(len(s)):
        if s[i] not in highlighted_chars:
            highlighted_chars.append(s[i])
    new_string = ""
    for char in s:
        if char in highlighted_chars:
            new_string += char * 2
        else:
            new_string += char
    return new_string
T = int(input())
for t in range(1, T+1):
    S = input().strip()
    strings = []
    for i in range(len(S)):
        highlighted_chars = []
        for j in range(i, len(S)):
            if S[j] not in highlighted_chars:
                highlighted_chars.append(S[j])
        new_string = ""
        for char in S:
            if char in highlighted_chars:
                new_string += char * 2
            else:
                new_string += char
        strings.append(new_string)
    print("Case #{}: {}".format(t, sorted(strings)[0]))