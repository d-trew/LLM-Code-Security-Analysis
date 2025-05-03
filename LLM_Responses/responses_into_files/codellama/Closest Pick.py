import math

def get_max_win_probability(n_tickets, k):
    # Calculate the number of possible combinations of two integers between 1 and K}
    num_combinations = int((k * (k + 1)) / 2)
    # Initialize a dictionary to store the count of each integer from 1 to K}
    count = {}
    for i in range(1, k+1):
        count[i] = 0
    # Increment the count of each integer in the list of tickets
    for ticket in n_tickets:
        for i in range(1, k+1):
            if ticket == i:
                count[i] += 1
    # Calculate the probability of winning for each combination of two integers
    win_probabilities = []
    for i in range(1, k+1):
        for j in range(i+1, k+1):
            if count[i] > 0 and count[j] > 0:
                win_probabilities.append((count[i]*count[j])/num_combinations)
    # Return the maximum probability of winning
    return max(win_probabilities)

def solve(n_tickets, k):
    # Get the maximum win probability by choosing the integers on your two tickets optimally
    max_win_probability = get_max_win_probability(n_tickets, k)
    return "{:.6f}".format(max_win_probability)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n_tickets = list(map(int, input().split()))
        k = int(input())
        print("Case #" + str(i+1) + ": " + solve(n_tickets, k))