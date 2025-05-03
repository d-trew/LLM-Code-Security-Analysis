def fractal_artwork(K, C):
    artwork = [''] * K
    for c in range(C):
        new_artwork = ''
        for tile in artwork:
            if 'L' in tile:
                new_artwork += (K*['L'] + tile)[1:]
            else:
                new_artwork += tile + K*'G'
        artwork = new_artwork
    return artwork

def check_for_gold(K, C):
    for c in range(C):
        complexity = 0
        while complexity < C:
            if 'G' in fractal_artwork(K, complexity)[K//2]:
                return [1]
            complexity += 1
    return ['IMPOSSIBLE']

for t in range(int(input())):
    K, C, S = map(int, input().split())
    print('Case #{}: {}'.format(t+1, check_for_gold(K, C)))