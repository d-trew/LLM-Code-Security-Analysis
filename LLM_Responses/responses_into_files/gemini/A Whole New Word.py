def solve():
    N, L = map(int, input().split())
    words = [input() for _ in range(N)]

    tiles = {}
    for word in words:
        for i, char in enumerate(word):
            if i + 1 not in tiles:
                tiles[i + 1] = set()
            tiles[i + 1].add(char)

    if L == 1:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            valid = True
            if char in "".join(words):
                valid = False
            if valid:
                return char
        return "-"

    
    def find_new_word():
        for i in range(len(words)):
          for j in range(i+1, len(words)):
            new_word = ""
            different = False
            for k in range(L):
              if words[i][k] != words[j][k]:
                different = True
                new_word += words[i][k]
              
            if different:
              valid = True
              for idx in range(L):
                if new_word[idx] not in tiles[idx+1]:
                  valid = False
                  break
              if valid and new_word not in words:
                return new_word
        return None

    new_word = find_new_word()
    if new_word:
        return new_word
    else:
        return "-"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")