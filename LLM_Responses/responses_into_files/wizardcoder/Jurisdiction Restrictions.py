def main():
    cases = int(input())
    for t in range(cases):
        R, C, S = map(int, input().split())
        stations = []
        for i in range(S):
            Ri, Ci, Di = map(int, input().split())
            stations.append((Ri, Ci, Di))
        
        assignments = [0] * S
        remaining_blocks = R * C - sum([1 for (Ri, Ci, Di) in stations if Ri == 1 and Ci == 1])
        for i in range(S):
            Ri, Ci, Di = stations[i]
            assignments[i] += sum([1 for r in range(max(1, Ri - Di + 1), min(Ri + Di, R)) for c in range(max(1, Ci - Di + 1), min(Ci + Di, C))])
        max_assignment = max(assignments)
        min_assignment = min(assignments)
        
        print("Case #%d: %d" % (t+1, max_assignment-min_assignment))

main()