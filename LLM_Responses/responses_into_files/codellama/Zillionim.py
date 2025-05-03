import random

def play_game():
    num_coins = 50
    num_moves = 10
    moves = []
    for i in range(num_moves):
        moves.append(random.randint(1, num_coins))
    return moves

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        num_games = int(input())
        for i in range(num_games):
            moves = play_game()
            print(" ".join(map(str, moves)))