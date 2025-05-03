import sys

def get_spanning_trees(n):
    trees = []
    for i in range(1, n+1):
        tree = []
        for j in range(1, n+1):
            if i != j:
                tree.append([i, j])
        trees.append(tree)
    return trees

def get_different_spanning_trees(n, k):
    trees = get_spanning_trees(n)
    different_trees = []
    for i in range(k):
        tree = []
        for j in range(len(trees)):
            tree.append(trees[j][i])
        different_trees.append(tree)
    return different_trees

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        trees = get_different_spanning_trees(n, k)
        print("Case #" + str(i+1) + ": " + str(len(trees)))
        for tree in trees:
            print(*tree, sep='')

if __name__ == "__main__":
    main()