import itertools

def generate_latin(n):
    elements = range(1, n+1)
    for perm in itertools.permutations(elements):
        if len(set(perm)) == n and len(set(zip(*perm))) == n:
            return perm
    return None

def main():
    T = int(input())
    for i in range(1, T+1):
        N, K = map(int, input().split())
        if K < N or K > N*N:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            latin_square = generate_latin(N)
            if not latin_square:
                print("Case #{}: IMPOSSIBLE".format(i))
            else:
                trace = sum([latin_square[x][x] for x in range(N)])
                while trace != K:
                    latin_square = generate_latin(N)
                    if not latin_square:
                        print("Case #{}: IMPOSSIBLE".format(i))
                        break
                    else:
                        trace = sum([latin_square[x][x] for x in range(N)])
                if trace == K:
                    print("Case #{}: POSSIBLE".format(i))
                    for row in latin_square:
                        print(*row)

if __name__ == "__main__":
    main()