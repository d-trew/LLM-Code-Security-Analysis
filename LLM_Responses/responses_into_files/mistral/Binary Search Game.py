from math import ceil
from typing import List
import sys
input = sys.stdin.readline
MOD = 1000000007

def binary_search(board, cards):
    n, m, l = len(board), len(cards), len(board) - 1
    half = (l + 1) // 2
    scores = [0] * MOD

    def game_score(index, remaining_cells, card_num):
        if not remaining_cells:
            return cards[card_num]
        left_half, right_half = remaining_cells[:index], remaining_cells[index:]
        if len(left_half) <= half:
            for i in range(m):
                game_score(sum(left_half), right_half, i)
        else:
            for i in range(m):
                game_score(sum(left_half[:half]), left_half[half:], i)

    for i in range(1, n + 1):
        for j in range(m):
            game_score(i - 1, board, j)

    return sum([scores[i] for i in range(MOD)]) % MOD

T = int(input())
for _ in range(T):
    n, m, l = map(int, input().split())
    board = [int(x) for x in bin(2 ** l)[2:].zfill(l)]
    print("Case #{}: {}".format(_ + 1, binary_search([0] + board, list(range(1, m + 1))))


This Python program calculates the sum of the scores of all M^N games by simulating each game and computing the score for each possible combination of cards. The `binary_search()` function takes a board with integers A_1, A_2, ... A_{2^L} in its cells and a list of card numbers as arguments and returns the sum of scores modulo 10^9+7 (MOD).

The input consists of the number of test cases T, followed by T lines, each containing three integers N, M, and L on the first line and 2^{L} integers A_1, A_2, ..., A_{2^L} on the second line. The output is a list of strings for each test case, where each string consists of "Case #x: y", where x is the test case number (starting from 1) and y is the sum of scores modulo MOD.