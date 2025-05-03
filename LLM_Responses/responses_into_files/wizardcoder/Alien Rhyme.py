def main():
    T = int(input()) # number of test cases
    for i in range(1, T+1):
        N = int(input()) # number of words
        words = []
        for j in range(N):
            words.append(input().upper()) # input the list of uppercase English letters representing each word
        
        max_pairs = 0
        for accent in range(len(words[0])):
            pairs = set()
            for k in range(N-1):
                for l in range(k+1, N):
                    if words[k][accent:] == words[l][accent:]: # check if suffixes are equal
                        pairs.add((k, l))
            max_pairs = max(max_pairs, len(pairs))
        
        print("Case #%d: %d" % (i, max_pairs*2))