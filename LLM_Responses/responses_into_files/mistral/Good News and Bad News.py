import sys
from collections import defaultdict

def get_input():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, p = map(int, sys.stdin.readline().split())
        graph = defaultdict(list)
        for _ in range(p):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
        news = solve(n, graph)
        if not news:
            print("Case #{}: IMPOSSIBLE".format(_ + 1))
        else:
            print("Case #{}: {}".format(_ + 1, ' '.join(str(v) for v in news)))

def solve(n, graph):
    news = [0] * n
    used = set()
    for i in range(1, n+1):
        if i not in used:
            news[i - 1], used.add(i) = distribute_news(graph, news, i)
    return news

def distribute_news(graph, news, friend):
        total = sum(news[:friend])
        total2 = sum(news[friend:])
        if abs(total - total2) > 2**31 or total == 0 or total2 == 0:
            return friend, []
        value = next((v for v in range(-2**31 + 1, 2**31) if (abs(v) <= 2**31 - friend and abs(total - v) <= 2**31)), None)
        if value is None:
            return friend, []
        news[friend - 1] = value
        for neighbor in graph[friend]:
            news[neighbor - 1] -= value
        return friend, [value]


This code reads test cases from the standard input and outputs the solution for each case. It uses a defaultdict to represent the graph of friends and their relationships, and it defines a solve function that recursively distributes news among the friends according to the given rules. The distribute\_news function checks if it's possible to assign a valid news value to a friend based on the current total sum of news received by that friend and the total sum of news given by that friend so far, and returns the friend and the news value if it finds one. If no valid news value can be found for a friend, the function returns an empty list for that friend's news value. The main function gets the input, solves each test case, and outputs the solution.