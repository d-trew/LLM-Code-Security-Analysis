import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for t in range(1, T+1):
        x, y, s = map(int, input().split())
        if x + y == 0:
            print(f"Case #{t}: 0")
            continue
        countCJ, countJC = 0, 0
        for c in s:
            if c == 'C' and s[s.index(c) - 1] == 'J':
                countCJ += 1
            elif c == 'J' and s[s.index(c) - 1] == 'C':
                countJC += 1
        if not (countCJ + countJC):
            print(f"Case #{t}: 0")
        else:
            min_cost = float('inf')
            for i in range(len(s)):
                if s[i] == '?':
                    new_s = s[:i] + ('C' if countJC > countCJ else 'J') + s[i+1:]
                    cost = sum((x if c == 'C' and new_s[new_s.index(c) - 1] == 'J' else 0 for c in new_s)) +\
                            sum((y if c == 'J' and new_s[new_s.index(c) - 1] == 'C' else 0 for c in new_s))
                    min_cost = min(min_cost, cost)
            print(f"Case #{t}: {min_cost}")

if __name__ == "__main__":
    solve()


This code reads the number of test cases and then iterates through each case. It calculates the total count of CJ and JC pairs in the current mural string, and if there are none, it prints 0 as the minimum cost. Otherwise, it iterates through the mural string to find the optimal way to fill in the empty spaces (represented by '?') such that the copyright cost is minimized. The optimization is done by checking all possible positions for filling in the empty space with either 'C' or 'J', and calculating the total cost of the resulting mural string, then taking the minimum cost found so far.