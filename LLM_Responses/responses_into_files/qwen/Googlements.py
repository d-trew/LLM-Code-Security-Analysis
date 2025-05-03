def count_possible_googlements(G):
    from collections import Counter
    
    def decay(g):
        counts = Counter(g)
        return ''.join(str(counts[str(i)]) for i in range(len(g) + 1))
    
    G_set = {G}
    while True:
        new_G_set = set(decay(g) for g in G_set)
        if not new_G_set - G_set:
            break
        G_set.update(new_G_set)
    
    return len(G_set)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        G = data[i]
        result = count_possible_googlements(G)
        results.append(f"Case #{i}: {result}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()