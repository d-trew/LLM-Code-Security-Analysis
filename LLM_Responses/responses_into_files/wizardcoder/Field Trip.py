import sys

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
def min_turns(positions):
    teacher = positions[0]
    kids = positions[1:]
    turns = 0
    while any([manhattan_distance(teacher, kid) > 1 for kid in kids]):
        new_kids = []
        for i in range(len(positions)):
            if manhattan_distance(teacher, positions[i]) > 1:
                teacher = [sum(x)//2 for x in zip(teacher, positions[i])]
                turns += 1
            else:
                new_kids.append(positions[i])
        kids = new_kids[:]
    return turns + len(kids) - 1
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        positions = []
        for j in range(N):
            R, C = map(int, input().split())
            positions.append((R, C))
        print("Case #%d: %d" % (i+1, min_turns(positions)))