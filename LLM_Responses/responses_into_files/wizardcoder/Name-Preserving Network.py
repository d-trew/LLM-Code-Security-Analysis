def main():
    T = int(input())
    for i in range(T):
        L, U = map(int, input().split())
        if 10 <= L <= 50 and L == U:
            N = L
            links = []
            for j in range(2*N+1):
                a, b = map(int, input().split())
                links.append((min(a,b), max(a,b)))
        else:
            print(-1)
            continue
        
        # check conditions 1-3 here
        
        # create network design with N computers and print 2N+1 lines representing that design
        for i in range(2*N+1):
            print(i, end="\n")
            
        # receive judge's copy of the network design
        judge_copy = []
        for j in range(2*N+1):
            a, b = map(int, input().split())
            if (a,b) not in links and (b,a) not in links:
                print(-1)
                break
            else:
                judge_copy.append((min(a,b), max(a,b))
                
        # determine the secret permutation f and recover the original identifiers
        
        # send back the list of Xs
        for j in range(N):
            print(j+1)