P = int(input())
for _ in range(P):
    P_i = list(map(int, input().split()))
    C = P_i[1]
    stacks = [list(map(lambda x: (int(x.split()[0]), int(x.split()[1])), input().split())) for _ in range(C)]
    N = int(input())
    case_id = 0
    for _ in range(N):
        N_i, C_i = map(int, input().split())
        premade_stack_indexes = list(map(int, input().split()))
        for i in premade_stack_indexes:
            if len(stacks[i]) > 1 and stacks[i][-2][0] == stacks[i][-1][0]:
                print("Case #{}: IMPOSSIBLE".format(case_id+1))
                case_id += 1
                break
        else:
            print("Case #{}: POSSIBLE".format(case_id+1))
            case_id += 1