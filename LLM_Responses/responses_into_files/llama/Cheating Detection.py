import numpy as np
from scipy.special import expit

T = int(input())
p = float(input())

for _ in range(T):
    skill_levels = np.random.uniform(-3.0, 3.0, size=100)
    question_difficulties = np.random.uniform(-3.0, 3.0, size=10000)
    answers = np.array([[int(expit(s-q)) for q in question_difficulties] for s in skill_levels])
    
    cheating_player = np.random.choice(100)
    cheating_results = (np.random.rand(10000) < 0.5).astype(int)
    answers[cheating_player-1, :] = (answers[cheating_player-1, :] + cheating_results).astype(int)
    
    correct_answers = np.sum(answers, axis=0)
    cheater_index = np.argmax(np.mean((correct_answers[:, None] == answers) & (answers != 2), axis=(0, 1)))
    print(f"Case #{_+1}: {cheater_index+1}")