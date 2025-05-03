def can_win_game(N, C, Pi):
    stacks = [premade_stacks[i] for i in Pi]
    for stack in stacks:
        values = [card[0] for card in stack]
        suits = [card[1] for card in stack]
        if len(set(values)) != 1 or len(set(suits)) != 1:
            return "IMPOSSIBLE"
    return "POSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    P = int(data[index])
    premade_stacks = []
    for _ in range(P):
        Ci = int(data[index + 1])
        stack = []
        index += 2
        for _ in range(Ci):
            Vij = int(data[index])
            Sij = int(data[index + 1])
            stack.append((Vij, Sij))
            index += 2
        premade_stacks.append(stack)
    
    T = int(data[index])
    results = []
    for i in range(T):
        N = int(data[index + 1])
        C = int(data[index + 2])
        Pi = list(map(int, data[index + 3:index + 3 + N]))
        index += 3 + N
        result = can_win_game(N, C, Pi)
        results.append(f"Case #{i+1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()