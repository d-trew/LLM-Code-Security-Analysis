import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def simulate_tournament(num_players, num_questions, skill_levels, question_difficulties, cheater=None):
    results = []
    for i in range(num_players):
        player_correct = [0] * num_questions
        for j in range(num_questions):
            if cheater is not None and i == cheater:
                flip = random.choice([True, False])
                if flip:
                    player_correct[j] = 1
                else:
                    player_correct[j] = 1 if random.random() > sigmoid(skill_levels[i] - question_difficulties[j]) else 0
            else:
                player_correct[j] = 1 if random.random() > sigmoid(skill_levels[i] - question_difficulties[j]) else 0
        results.append(player_correct)
    return results

def identify_cheater(results, num_players):
    for i in range(num_players):
        player_results = [sum(row[i] for row in results) / len(results)]
        if player_results[0] == 1.0:
            return i + 1
    return None

def main():
    T = int(input())
    P = int(input())
    for t in range(1, T + 1):
        num_players = 100
        num_questions = 10000
        skill_levels = [random.uniform(-3.00, 3.00) for _ in range(num_players)]
        question_difficulties = [random.uniform(-3.00, 3.00) for _ in range(num_questions)]
        cheater = random.randint(0, num_players - 1)
        results = simulate_tournament(num_players, num_questions, skill_levels, question_difficulties, cheater)
        cheater_id = identify_cheater(results, num_players)
        print(f"Case #{t}: {cheater_id}")

if __name__ == "__main__":
    main()