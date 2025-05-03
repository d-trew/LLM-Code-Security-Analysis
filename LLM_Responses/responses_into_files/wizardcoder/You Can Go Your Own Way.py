import sys

def find_path(n, lydia_path):
    path = []
    for i in range(n*n-1):
        if i % n == 0 and (i+1) % n != 0: # Moving south is allowed
            path.append("S")
        elif (i+1) % n == 0 and i % n != 0: # Moving east is allowed
            path.append("E")
        else:
            if lydia_path[i] == "E": # Lydia moved south, we can move east
                path.append("E")
            elif lydia_path[i] == "S": # Lydia moved east, we can move south
                path.append("S")
    return "".join(path)

def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        lydia_path = input()
        my_path = find_path(n, lydia_path)
        print("Case #{}: {}".format(i, my_path))

if __name__ == "__main__":
    main()