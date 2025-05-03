import sys

def main():
    t = int(input())
    for i in range(t):
        n, l = map(int, input().split())
        words = []
        for j in range(n):
            word = input()
            words.append(word)
        new_words = []
        for j in range(l):
            new_words.append(input())
        for word in new_words:
            if word not in words:
                print("Case #" + str(i+1) + ": " + word)
                break
        else:
            print("Case #" + str(i+1) + ": -")

if __name__ == '__main__':
    main()