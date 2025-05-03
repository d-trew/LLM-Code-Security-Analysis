def min_turns(N, people):
    teacher = people[0]
    kids = people[1:]
    
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def min_moves_to_gather(kids, teacher):
        if not kids:
            return 0
        min_turns = float('inf')
        for kid in kids:
            moves = manhattan_distance(teacher, kid) + min_moves_to_gather([k for k in kids if k != kid], kid)
            min_turns = min(min_turns, moves)
        return min_turns
    
    return min_moves_to_gather(kids, teacher)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        people = [(int(data[index + 2 * i]), int(data[index + 2 * i + 1])) for i in range(N)]
        index += 2 * N
        result = min_turns(N, people)
        results.append(f"Case #{_ + 1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()