import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def main():
    T = int(input())
    P = float(input())
    for i in range(T):
        correct_answers = []
        cheater = -1
        players = [[] for _ in range(100)]
        for j in range(1, 101):
            skill_levels = list(map(float, input().split()))
            question_difficulty = float(input())
            cheater_probability = sum([sigmoid(skill - question_difficulty) for skill in skill_levels]) / 100
            if random.random() < cheater_probability:
                cheater = j
            else:
                correct_answers.extend([int(x) for x in input().split()])
        for player, answers in enumerate(players):
            if sum(1 for answer in correct_answers[:j] if answer == 0) / len(correct_answers[:j]) >= P:
                cheater = player + 1
                break
        print("Case #{}: {}".format(i+1, cheater))
            
if __name__ == "__main__":
    main()