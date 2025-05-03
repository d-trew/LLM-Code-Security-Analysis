def min_exchanges(C, J, activitiesC, activitiesJ):
    total_time = 24 * 60
    cameron_time = [False] * total_time
    jamie_time = [False] * total_time
    
    for start, end in activitiesC:
        for i in range(start, end):
            cameron_time[i] = True
    
    for start, end in activitiesJ:
        for i in range(start, end):
            jamie_time[i] = True
    
    exchanges = 0
    current_cameron = False
    current_jamie = False
    
    for t in range(total_time):
        if cameron_time[t]:
            if not current_cameron and current_jamie:
                exchanges += 1
            current_cameron = True
        else:
            current_cameron = False
        
        if jamie_time[t]:
            if not current_jamie and current_cameron:
                exchanges += 1
            current_jamie = True
        else:
            current_jamie = False
    
    return exchanges

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        C = int(data[index])
        J = int(data[index + 1])
        index += 2
        
        activitiesC = []
        for _ in range(C):
            start = int(data[index]) * 60
            end = int(data[index + 1]) * 60
            activitiesC.append((start, end))
            index += 2
        
        activitiesJ = []
        for _ in range(J):
            start = int(data[index]) * 60
            end = int(data[index + 1]) * 60
            activitiesJ.append((start, end))
            index += 2
        
        result = min_exchanges(C, J, activitiesC, activitiesJ)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()