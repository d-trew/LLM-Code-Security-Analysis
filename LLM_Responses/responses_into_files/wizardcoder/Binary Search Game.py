for _ in range(int(input())):
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    board_size = 2**L
    scores = []
    
    for i in range(M):
        referee = [i+1]*N if i < M-1 else [N]
        alice_score = 0
        bob_score = 0
        
        for j in range(L//2):
            alice_choices = []
            bob_choices = []
            
            for k in range(board_size // 2**(j+1)):
                if A[k] > A[-1-k]:
                    alice_choices.append((A[k], A[-1-k]))
                else:
                    bob_choices.append((A[k], A[-1-k]))
            
            for a, b in alice_choices:
                if a < referee[0]:
                    alice_score += b
                else:
                    bob_score += a
            
            board = [x for x in A if x not in alice_choices and x not in bob_choices]
            board.sort(reverse=True)
            
        scores.append((alice_score + bob_score) % (10**9+7))
    
    print("Case #%d: %d" % (_+1, sum(scores)))