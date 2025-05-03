import random
import sys

def main():
    T = int(input())
    W = int(input())
    games_won = 0

    for i in range(T):
        coins = list(range(1, 51))
        ai_turns = True
        while len(coins) >= 10:
            if ai_turns:
                valid_moves = []
                for j in range(len(coins) - 9):
                    if all([x not in coins for x in range(coins[j], coins[j] + 10)]):
                        valid_moves.append(coins[j])
                move = random.choice(valid_moves)
                print(move)
                sys.stdout.flush()
                ai_turns = False
            else:
                p = int(input())
                if p == -1:
                    break
                coins = [x for x in coins if x not in range(p, p + 10)]
                ai_turns = True
        else:
            games_won += 1

        if games_won >= W:
            print("I win!")
            sys.exit()

if __name__ == "__main__":
    main()