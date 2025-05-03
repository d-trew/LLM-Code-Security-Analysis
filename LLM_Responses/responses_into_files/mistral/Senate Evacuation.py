import sys
input = sys.stdin.readlines

def solve(n):
    parties = [int(x) for x in input()[1].split()]
    senators = [0]*26
    for senator, party in enumerate(parties):
        senators[ord(chr(ord('A')+senator))-ord('A')] += party

    while True:
        majority_party = -1
        max_count = 0
        for i in range(26):
            if senators[i] > max_count:
                max_count = senators[i]
                majority_party = i
        if max_count <= len(parties)//2:
            break
        min_count = max_count+1
        for i in range(26):
            if senators[i] < min_count and senators[i] > 0:
                min_count = senators[i]
        index = -1
        for i in range(26):
            if senators[i] == min_count:
                if index == -1 or senators[index] > senators[i]:
                    index = i
        to_evacuate = chr(ord('A')+index)
        if index != majority_party:
            to_evacuate += chr(ord('A')+majority_party)
        for party in to_evacuate:
            senators[ord(party)-ord('A')] -= 1
        print("Case #{}: {}".format(n, ' '.join(to_evacuate)))
        senators = [0]*26
        parties = [int(x) for x in input()]

T = int(input()[0])
for t in range(1, T+1):
    solve(t)

This Python code takes the number of test cases as input and iterates through each test case. For each test case, it first reads the number of parties and their respective senators from the input. Then it initializes an array to store the count of senators for each party, where the index corresponds to the ASCII value of the party's corresponding uppercase letter.
Next, it enters a loop that continues until no party has an absolute majority. In each iteration of this loop, it finds the party with the maximum number of senators and checks if it exceeds half of the total number of senators. If not, it breaks from the loop. Otherwise, it finds the party with the minimum number of senators that is greater than zero and less than or equal to the maximum count. It then selects the pair of parties to evacuate based on these two conditions. Finally, it updates the senator counts for the chosen parties and prints the evacuation plan for the test case. The code repeats this process for each test case until all cases have been processed.