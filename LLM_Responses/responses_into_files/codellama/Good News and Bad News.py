import sys

def get_input():
    return sys.stdin.readline().strip()

def solve(F, P):
    friends = {i for i in range(1, F+1)}
    pairs = []
    for _ in range(P):
        a, b = map(int, get_input().split())
        if a == b: continue
        pairs.append((a, b))
        friends.remove(a)
        friends.remove(b)
    
    # check if the number of friends is even
    if len(friends) % 2 != 0:
        return "IMPOSSIBLE"
    
    news = [0] * P
    for i in range(P):
        a, b = pairs[i]
        if news[i-1] == -news[i-1]:
            return "IMPOSSIBLE"
        
        # check if the absolute value is less than F2
        if abs(news[i-1]) > 32:
            return "IMPOSSIBLE"
        
        # check if the friend can talk to each other
        if a not in friends or b not in friends:
            return "IMPOSSIBLE"
    
    return news

if __name__ == '__main__':
    T = int(get_input())
    for t in range(1, T+1):
        F, P = map(int, get_input().split())
        print(f"Case #{t}: {solve(F, P)}")