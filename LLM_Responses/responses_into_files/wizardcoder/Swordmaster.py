def main():
    T = int(input())
    for i in range(1, T+1):
        N, P = map(int, input().split())
        A = list(map(int, input().split()))
        D = list(map(int, input().split())
        opponents_known_attacks = []
        for _ in range(N):
            opponent_info = input().split()
            known_attacks = set(map(int, opponent_info[:P])
            opponents_known_attacks.append(known_attacks)
        
        # TODO: implement the rest of the code to determine if it is possible for you to become Swordmaster
        print("Case #{}: {}".format(i, "YES" if can_become_swordmaster else "NO"))
        
main()