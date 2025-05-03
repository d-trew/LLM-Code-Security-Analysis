from collections import Counter
import string

def find_digit_string(queries):
    letters = list(string.ascii_uppercase)
    count = Counter()
    for _ in range(10):
        count[letters.pop(max(count, key=count.get))] -= 1
    digit_string = ''.join(sorted(letters))

    server_mapping = {digit_string[i]: i for i in range(10)}

    responses = [[] for _ in range(104)]
    for query in queries:
        if query[0] != -1:
            responses[query[0]].append((query[0], server_mapping[query[1][0]]))
        else:
            responses[-1].append((query[1], None))

    frequencies = Counter()
    for query, response in responses:
        if response is not None:
            for i, digit in enumerate(response):
                frequencies[server_mapping.get(digit)] += 1

    for i, frequency in enumerate(frequencies):
        if frequency != len(responses) - sum([q[0] == -1 for q in responses]):
            return "Case #1: {}".format(''.join(server_mapping.values()))

    for i in range(2, 17):
        new_responses = [[(query[1], response) for query, response in res] for res in zip(*sorted(responses[:i] + responses[i:]))]
        frequencies = Counter()
        for query, response in new_responses:
            if response is not None:
                for j, digit in enumerate(response):
                    frequencies[server_mapping.get(digit)] += 1

        for i, frequency in enumerate(frequencies):
            if frequency != len(new_responses[i]) - sum([q[0] == None for q in new_responses[i]]):
                return "Case #{}: {}".format(i + 1, ''.join(server_mapping.values()))

    return "Case #17: UNKNOWN"


This code finds the secret digit string for each server based on the collected data. It first generates a random digit string with 10 unique letters and maps them to digits 0 through 9. Then it processes the queries, groups them by their corresponding servers, and counts the frequency of each letter used in the responses from each server. Finally, it checks if the frequencies match the expected values for each server and returns the digit string for those that do. If no solution is found after checking all servers, it returns "UNKNOWN" for the 17th test case.