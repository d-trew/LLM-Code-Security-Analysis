import math

def prime_time(deck):
    # Find the primes in the deck
    primes = set()
    for card in deck:
        if math.sqrt(card) % 1 == 0:
            primes.add(card)
    
    # Calculate the score for each possible split
    scores = {}
    for prime in primes:
        score = 0
        for card in deck:
            if card % prime == 0:
                score += prime
        scores[prime] = score
    
    # Find the maximum score
    max_score = 0
    for prime, score in scores.items():
        if score > max_score:
            max_score = score
    
    return max_score

# Test cases
def test_cases(T):
    for tc in range(1, T+1):
        # Input: M, P_i, N_i
        M = int(input())
        deck = []
        for i in range(M):
            P_i, N_i = map(int, input().split())
            for j in range(N_i):
                deck.append(P_i)
        
        # Output: Case #x: y
        print("Case #" + str(tc) + ": " + str(prime_time(deck)))

# Main function
def main():
    T = int(input())
    test_cases(T)

if __name__ == '__main__':
    main()