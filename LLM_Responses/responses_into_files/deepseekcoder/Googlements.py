def googlement_count(G):
    L = len(G)
    count_dict = {0: [1]}
    for i in range(10):
        if i > L:
            break
        new_count_dict = {}
        for googlement, counts in count_dict.items():
            for j in range(L+1):
                if str(i) * (j + 1) == G[:j+1]:
                    new_counts = list(counts)
                    new_counts.append(int(''.join(map(str, counts))))
                    new_count_dict.setdefault(0, []).append(new_counts)
        count_dict = new_count_dict
    return len(count_dict[0])

T = int(input())
for i in range(T):
    G = input()
    print(f"Case #{i+1}: {googlement_count(G)}")