def main():
    T = int(input())
    for i in range(T):
        C = int(input())
        camps = []
        for j in range(1, 2*C+1):
            E, L, D = map(int, input().split())
            camps.append((E, L, D))
        
        total_time = 0
        for tour in camps:
            if tour[0] == 1:
                total_time += tour[2] - tour[1] + 24
            else:
                total_time += tour[2] - tour[1]
        
        print("Case #%d: %d" % (i+1, total_time))

main()