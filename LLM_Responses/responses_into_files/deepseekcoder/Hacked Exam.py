Here is a Python program based on your description:


from fractions import Fraction
import sys

def solve():
    n, q = map(int, input().split())
    scores = [0]*q
    for _ in range(n):
        s, ans = input().split()
        s = int(s)
        for i in range(q):
            if ans[i] == 'T':
                scores[i] += Fraction(1)/Fraction(2)**int(ans[i]) * 2 - 1
    return " ".join([str((scores.index(max(scores)), max(scores))) for _ in range(q)] + [str(sum(scores))])

t = int(input())
for i in range(1, t+1):
    print("Case #{}: {}".format(i, solve()))

This program uses the concept of expected value and probability to calculate the maximum expected score. It reads the number of students (n) and questions (q). For each student, it calculates their score based on whether they answered 'T' or 'F'. The scores are stored in a list. Finally, it prints out the index of the question with the highest score along with the score itself.