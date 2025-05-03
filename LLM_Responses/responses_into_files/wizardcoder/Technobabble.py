import random

def is_fake(topics):
    for i in range(len(topics)):
        if topics[i] in [' '.join([topics[j][1], topics[j][0]) for j in range(len(topics))]:
            return False
    return True

def max_fakes():
    N = int(input())
    cases = []
    for i in range(N):
        topics = [input().split() for _ in range(int(input()))]
        if is_fake(topics):
            cases.append(len(topics))
        else:
            cases.append(-1)
    return cases

def main():
    T = int(input())
    for i in range(T):
        print("Case #%d: %d" % (i+1, max_fakes()[i]) if max_fakes()[i] != -1 else "Case #%d: 0" % (i+1))
    
if __name__ == '__main__':
    main()