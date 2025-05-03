import sys

def main():
    T = int(input())
    for case in range(T):
        R, C = map(int, input().split())
        grid = [list(input()[:C]) for _ in range(R)]
        
        # your code here to assign cake pieces to children
        
        print("Case #{}:".format(case+1))
        for row in grid:
            print(''.join(row))
    
if __name__ == "__main__":
    main()