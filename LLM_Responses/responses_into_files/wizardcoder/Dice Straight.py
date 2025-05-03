import sys
from collections import defaultdict

def longest_straight(dice):
    faces = []
    for die in dice:
        faces.extend(die)
    freq = defaultdict(int)
    for face in faces:
        freq[face] += 1
    
    max_straight = 0
    for i in range(1, 7):
        if freq[i]:
            current_straight = 1
            for j in range(i+1, 7):
                if freq[j] and (freq[i] > 0 or freq[j] > 0):
                    current_straight += 1
            max_straight = max(max_straight, current_straight)
    
    return max_straight

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        dice = []
        
        for _ in range(N):
            die = list(map(int, input().split()))
            dice.append(die)
        
        print("Case #%d: %d" % (i+1, longest_straight(dice))
    
if __name__ == "__main__":
    main()