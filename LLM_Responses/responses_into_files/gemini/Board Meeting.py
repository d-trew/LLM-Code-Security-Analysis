T, Nmax, M, R = map(int, input().split())

def get_total_moves(A, B):
    print(A, B)
    response = input()
    if response == 'ERROR':
        exit()
    return int(response)

def answer_query(C, D):
    total_moves = 0
    for i in range(len(queries)):
        total_moves += max(abs(queries[i][0]-C), abs(queries[i][1]-D))
    print(total_moves)
    response = input()
    if response == 'ERROR':
        exit()


for t in range(T):
    queries = []
    
    #Phase 1
    A = 0
    B = 0
    for i in range(R):
        total_moves = get_total_moves(A,B)
        queries.append((A,B))
        A += 100000
        B+=100000

    print("READY")

    #Phase 2
    while True:
        try:
            C, D = map(int, input().split())
            answer_query(C,D)
        except EOFError:
            break
        except ValueError:
            break