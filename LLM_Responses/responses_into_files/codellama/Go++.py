T = int(input())
for _ in range(T):
    N, L = map(int, input().split())
    G = [input() for _ in range(N)]
    B = input()
    print(f"Case #{_+1}: {'IMPOSSIBLE' if (B in G) else ''.join(['?0', '?1'][:L])}")