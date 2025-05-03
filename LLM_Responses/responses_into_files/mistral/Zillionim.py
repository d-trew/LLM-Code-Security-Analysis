import random

def play_game():
    n = int(input().split()[0])
    w = int(input().split()[0])
    games_won = 0

    for _ in range(n):
        coins = list(range(1, 51))
        ai_move = None
        while True:
            move = random.sample(coins, 10)
            if all(c not in move for c in coins[:10]):
                ai_move = move[0] + min(move) - 1
                break

        p = int(input())
        if p == -1:
            return
        q = int(input().split()[0])
        if q in ai_move or q > coins[-1] - 9 or ai_move[-1] + 10 >= q:
            print(-1)
            return
        coins[q:q+10] = []
        if len(coins) < 11:
            print(-2)
            return
        if not coins:
            games_won += 1
            break

    if games_won >= w:
        print("Case #1: True")
    else:
        print("Case #1: False")

play_game()