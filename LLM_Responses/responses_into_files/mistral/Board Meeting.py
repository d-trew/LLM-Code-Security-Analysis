from sys import stdin, stdout

def main():
    cases = int(stdin.readline().strip())

    for _ in range(cases):
        N, M, R = map(int, stdin.readline().split())
        kings = set()
        for _ in range(N):
            x, y = map(int, stdin.readline().split())
            kings.add((x, y))

        for _ in range(R):
            x, y = map(int, stdin.readline().split())
            total_moves = sum([max(abs(xi - x), abs(yi - y)) for xi, yi in kings])
            stdout.write(f"{total_moves}\n")

        stdout.write("READY\n")

        for _ in range(R):
            x, y = map(int, stdin.readline().split())
            total_moves = sum([max(abs(xi - x), abs(yi - y)) for xi, yi in kings])
            stdout.write(f"{total_moves}\n")

        stdout.write("DONE\n")

if __name__ == "__main__":
    main()

This code reads the number of test cases and processes each one according to the problem description. The first phase involves making R requests to the judge, calculating the total number of moves for each request, and sending the result back to the judge. In the second phase, the roles are reversed, and the judge sends requests to the program, which calculates the total number of moves and responds accordingly. The program ends when all test cases have been processed or an error occurs.