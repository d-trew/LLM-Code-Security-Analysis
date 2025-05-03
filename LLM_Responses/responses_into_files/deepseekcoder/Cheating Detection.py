import numpy as np
from scipy.special import expit  # Sigmoid function

def sigmoid(x):
    return expit(x)

def generate_skills_questions():
    skills = np.random.uniform(-3, 3, size=100)
    questions = np.random.uniform(-3, 3, size=10000)
    return skills, questions

def calculate_probabilities(skill, question):
    return sigmoid(skill - question)

def generate_answers(skills, questions):
    answers = []
    for i in range(len(questions)):
        answer = np.random.binomial(n=1, p=calculate_probabilities(skills[i], questions[i]), size=100)
        answers.append(answer)
    return np.array(answers).T  # Transpose to match the format of input

def cheat(player_answer):
    return np.random.binomial(n=1, p=0.5, size=len(player_answer))

def identify_cheater(players_answers, player_count):
    for i in range(player_count):
        if sum(players_answers[:,i]) == len(players_answers[0]):  # All questions answered correctly
            return i + 1  # Adding 1 to match the player numbers starting from 1
    return -1  # Return -1 if no cheater is found

def tournament():
    T = int(input())
    P = float(input()) / 100
    
    for t in range(T):
        skills, questions = generate_skills_questions()
        players_answers = generate_answers(skills, questions)
        
        # Cheat with 50% probability
        cheating_probs = np.random.binomial(n=1, p=0.5, size=len(players_answers[0]))
        for i in range(len(players_answers)):
            if cheating_probs[i]:  # If player is going to cheat
                players_answers[i] = cheat(players_answers[i])
        
        cheater = identify_cheater(players_answers, len(skills))
        print("Case #{}: {}".format(t+1, cheater if cheater != -1 else "Cannot determine"))