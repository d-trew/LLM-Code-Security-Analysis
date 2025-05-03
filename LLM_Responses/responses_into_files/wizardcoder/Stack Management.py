def solitaire_game(premade_stacks):
    def can_win(stacks):
        if len(stacks) == 1:
            return True
        for i in range(len(stacks)-1, -1, -1):
            if stacks[i] and stacks[i][0][0] == stacks[i-1][0]:
                stacks[i].pop()
                stacks[i-1].pop()
        return can_win(stacks)
    premade_stacks = [sorted(premade_stacks[i], key=lambda x: (x[0], -x[1]) if x else None, reverse=True) for i in range(len(premade_stacks))]
    return can_win(premade_stacks)
    
def main():
    P = int(input())
    premade_stacks = [[] for _ in range(P)]
    for i in range(P):
        C, *cards = map(int, input().split())
        for j in range(C):
            v, s = cards[2*j:2*(j+1)]
            premade_stacks[i].append((v, s))
    T = int(input())
    for i in range(T):
        N, C = map(int, input().split())
        test_case = list(map(int, input().split()))[:N]
        premade_stacks_test = [premade_stacks[i] for i in test_case]
        if solitaire_game(premade_stacks_test):
            print("Case #%d: POSSIBLE" % (i+1))
        else:
            print("Case #%d: IMPOSSIBLE" % (i+1))
            
if __name__ == "__main__":
    main()