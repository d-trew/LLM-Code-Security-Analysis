from itertools import accumulate
import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        A, J = map(int, input().split())
        C = [list(map(int, input().split())) for _ in range(A)]
        J_activities = [list(map(int, input().split())) for _ in range(J)]

        total_cameron = sum([d - c for c, d in C])
        total_jamie = sum([k - j for j, k in J_activities])

        if total_cameron > 720 or total_jamie > 720:
            print(f"Case #{_+1}: Impossible")
            continue

        activities = sorted((C, J_activities), key=lambda x: sum([a[1] for a in x]) - sum([a[0] for a in x]))
        A, J = activities[0], activities[1]

        if total_cameron + total_jamie > 720:
            print(f"Case #{_+1}: Impossible")
        else:
            Cameron, Jamie = 0, 0
            exchanges = 0

            for c, d in A:
                Jamie += d - c
                if Jamie > 720:
                    print(f"Case #{_+1}: Impossible")
                    break

            for j, k in reversed(Jamie):
                Cameron += k - j
                if Cameron > 720:
                    print(f"Case #{_+1}: Impossible")
                    break

                if (Cameron <= 720 and Jamie <= 720) and (Cameron + Jamie > 720):
                    exchanges += 1
                    Cameron, Jamie = 720 - Cameron, 720 - Jamie

            print(f"Case #{_+1}: {exchanges}")

solve()