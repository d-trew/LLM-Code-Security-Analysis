import sys
from collections import deque
input = sys.stdin.readline
T, N, W = map(int, input().split())

def play_game():
    north, south = [[] for _ in range(2*N)], [[] for _ in range(2*N)]
    score = 0
    for _ in range(N):
        a, b = map(int, input().split())
        north[b-1] += [a-1]
        south[a-1] += [b-1]
        if not north[b-1]: score += len([r for r in reversed(north[:b]) if r])
        if not south[a-1]: score += len([r for r in reversed(south[:a]) if r])
    return score, [north, south]

def opponent_move():
    trees = list(range(2*N))
    for i in range(N):
        a, b = play_game()[1][b]
        c, d = play_game()
        yield (a, b), (c, d)
        trees[c-1], trees[d-1] = trees[b-1], trees[a-1]

def main():
    wins = 0
    for _ in range(T):
        score, _ = play_game()
        if score > max((opponent_move().__next__(), opponent_move().__next__())[0][1]):
            print(*zip(*opponent_move()))
            wins += 1
    print(wins)

main()