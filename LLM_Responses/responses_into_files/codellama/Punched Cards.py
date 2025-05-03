import sys

def punched_card(R, C):
    # Top row
    top = '+' + '-' * (C - 1) + '+\n'
    
    # Middle rows
    middle = []
    for i in range(R - 2):
        line = '| ' + '. ' * (C - 2) + '|\n'
        middle.append(line)
    
    # Bottom row
    bottom = '+' + '-' * (C - 1) + '+\n'
    
    return top + ''.join(middle) + bottom

if __name__ == "__main__":
    input = sys.stdin.read()
    R, C = map(int, input.split())
    print("Case #1:")
    print(punched_card(R, C))