import sys

def main():
    T = int(input())
    for i in range(1, T+1):
        R, C = map(int, input().split())
        S = []
        for j in range(R):
            row = list(map(int, input().split()))
            S.append(row)
        interest_level = 0
        while True:
            eliminated = False
            new_S = [[] for _ in range(R)]
            for j in range(C):
                for k in range(R):
                    if S[k][j] == -1: continue
                    neighbors = 0
                    neighbor_sum = 0
                    if k > 0 and S[k-1][j] != -1:
                        neighbors += 1
                        neighbor_sum += S[k-1][j]
                    if k < R-1 and S[k+1][j] != -1:
                        neighbors += 1
                        neighbor_sum += S[k+1][j]
                    if j > 0 and S[k][j-1] != -1:
                        neighbors += 1
                        neighbor_sum += S[k][j-1]
                    if j < C-1 and S[k][j+1] != -1:
                        neighbors += 1
                        neighbor_sum += S[k][j+1]
                    
                    if neighbors > 0 and S[k][j]/neighbors < neighbor_sum/neighbors:
                        S[k][j] = -1
                        eliminated = True
                        
            for j in range(C):
                for k in range(R):
                    if S[k][j] == -1: continue
                    new_S[k].append(S[k][j])
                    
            if not any([len(x) > 0 for x in new_S]): break
            
            interest = sum([sum(x) for x in S])
            interest_level += interest
            S = new_S
        print("Case #{}: {}".format(i, interest_level))

if __name__ == "__main__":
    main()