import itertools
T = int(input())
for _ in range(T):
    S = int(input())
    K = 3
    while True:
        for L in range(1, (S//10)+2):
            for P in itertools.product('0123456789', repeat=L):
                P_str = ''.join(P)
                if int(P_str) <= S:
                    if K == 1:
                        print(f'Case #{"":_;}: {P_str}')
                        break
                    else:
                        S -= int(P_str)
                        K -= 1
                        if K > 0:
                            for L2 in range(1, (S//10)+2):
                                for P2 in itertools.product('0123456789', repeat=L2):
                                    P2_str = ''.join(P2)
                                    if int(P2_str) <= S:
                                        if K == 2:
                                            print(f'Case #{"":_;}: {P_str}{P2_str}')
                                            break
                                        else:
                                            S -= int(P2_str)
                                            K -= 1
                                            if K > 0:
                                                for L3 in range(1, (S//10)+2):
                                                    for P3 in itertools.product('0123456789', repeat=L3):
                                                        P3_str = ''.join(P3)
                                                        if int(P3_str) <= S:
                                                            print(f'Case #{"":_;}: {P_str}{P2_str}{P3_str}')
                                                            break
                                        break
                                else:
                                    continue
                            else:
                                continue
                        else:
                            break
                else:
                    continue
        else:
            break