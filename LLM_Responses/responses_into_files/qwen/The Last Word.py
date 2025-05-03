def last_word(s):
    from collections import deque
    q = deque()
    for char in s:
        while q and q[-1] < char:
            q.pop()
        q.append(char)
    return ''.join(q)

t = int(input())
for i in range(1, t + 1):
    s = input().strip()
    print(f"Case #{i}: {last_word(s)}")