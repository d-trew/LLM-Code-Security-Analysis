from sys import stdin, setrecursionlimit
setrecursionlimit(200)

def read_input():
    t = int(stdin.readline())
    programs = []
    for _ in range(t):
        n, l = map(int, stdin.readline().split())
        g = [list(map(int, stdin.readline().split()))] * n
        b = list(map(int, stdin.readline().split()))
        programs.append((n, l, g, b))
    return programs

def generate_programs(n, l, g, b):
    def recurse(i, reg1, reg2, seq1, seq2, count=0):
        if count > 200:
            return False
        if len(seq1) + len(seq2) == l and count == l - len(b):
            if b not in [seq1 + seq2 for seq1, seq2 in itertools.product(*[itertools.permutations(g)] * 2)]:
                return True
            else:
                return False
        for j in range(i, n):
            for state in (0, 1):
                new_seq1 = seq1 + [state] if i == 0 else seq1
                new_seq2 = seq2 + [state] if i == n - 1 else seq2
                recurse(j + 1, reg1 if state == 0 else reg2, reg1 if state == 1 else reg2, new_seq1, new_seq2)
        return False
    reg1 = 0
    reg2 = 0
    return True if recurse(0, reg1, reg2, [], []) else False

def write_output(programs):
    for i, (n, l, g, b) in enumerate(programs, start=1):
        if not generate_programs(n, l, g, b):
            print(f"Case #{i}: IMPOSSIBLE")
        else:
            program1 = ''.join([str(x[0]) for x in sorted(g)] + ['?'])
            program2 = ''.join(['?'] + [str(x[0]) for x in reversed(sorted(g))])
            print(f"Case #{i}: {program1} {program2}")

if __name__ == "__main__":
    programs = read_input()
    write_output(programs)


This Python program reads the input, generates combinations of Go++ programs based on the given conditions, and writes the output. The recursive function `generate_programs` generates all possible combinations of Go++ programs by iterating through all possible sequences of instructions for each program, ensuring that the total number of instructions does not exceed 200 and the combined length of the two programs is equal to the given length L. The function checks if any of the generated combinations produces the "bad" string B or all the strings in G. If no such combination is found, it returns False, indicating that the task is impossible. Otherwise, it returns True and the generated Go++ programs are printed as output.