import itertools

def main():
    T = int(input())
    for i in range(1, T+1):
        N, L = map(int, input().split())
        vincent_words = []
        for _ in range(N):
            vincent_words.append(input())
        
        # Get all possible combinations of Vincent's tiles
        all_tiles = [chr(x) + str(y+1) for x in range(ord('A'), ord('Z')+1) for y in range(L)]
        valid_tiles = []
        
        # Check if there is at least one valid tile combination
        for tiles in itertools.product(*[all_tiles]*N):
            if ''.join(tiles) not in vincent_words:
                valid_tiles.append(''.join(tiles))
        
        # Output the result
        if len(valid_tiles) > 0:
            print("Case #{}: {}".format(i, valid_tiles[0])
        else:
            print("Case #{}: -".format(i))

if __name__ == "__main__":
    main()