def solve():
    s, e = input().split()
    s_int = int(s, 2)
    e_int = int(e, 2)

    q = [(s_int, 0)]
    visited = {s_int}

    while q:
        curr_int, curr_dist = q.pop(0)
        if curr_int == e_int:
            return curr_dist

        # Double operation
        next_int = curr_int * 2
        if next_int not in visited and next_int <= 2**10:
            q.append((next_int, curr_dist + 1))
            visited.add(next_int)

        # NOT operation
        next_int = int("".join(["1" if bit == "0" else "0" for bit in bin(curr_int)[2:]]), 2) if curr_int > 0 else 1
        
        if next_int not in visited and next_int <= 2**10:
            q.append((next_int, curr_dist + 1))
            visited.add(next_int)

    return "IMPOSSIBLE"

t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")