def solve():
    A = int(input())
    opponents = [input() for _ in range(A)]

    def winner(p1, p2):
        i = 0
        j = 0
        while i < 10**100:
            m1 = p1[i % len(p1)]
            m2 = p2[j % len(p2)]
            if m1 == m2:
                i += 1
                j += 1
            elif (m1 == 'R' and m2 == 'S') or \
                 (m1 == 'S' and m2 == 'P') or \
                 (m1 == 'P' and m2 == 'R'):
                return 0  # p1 wins
            else:
                return 1  # p2 wins
        return 2 #draw


    def can_win(program):
        for i in range(1 << A):
            matchups = []
            for j in range(A):
                if (i >> j) & 1:
                    matchups.append(opponents[j])
                else:
                    matchups.append(opponents[j])

            
            
            wins = True
            
            current_round_winners = list(range(A+1))
            round_num = 0

            while len(current_round_winners)>1:
                next_round_winners = []
                for k in range(0, len(current_round_winners),2):
                  p1_index = current_round_winners[k]
                  p2_index = current_round_winners[k+1]

                  p1 = program if p1_index == A else matchups[p1_index]
                  p2 = program if p2_index == A else matchups[p2_index]


                  if winner(p1,p2) == 0:
                      next_round_winners.append(p1_index)
                  else:
                      next_round_winners.append(p2_index)
                current_round_winners = next_round_winners
                round_num +=1

            if current_round_winners[0] != A:
                wins = False
                break
        return wins

    for i in range(1, 501):
        for j in range(3**i):
            program = ""
            temp = j
            for _ in range(i):
                program = "RPS"[temp % 3] + program
                temp //= 3
            if can_win(program):
                return program
    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")