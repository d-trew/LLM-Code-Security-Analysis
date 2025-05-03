Here is a Python code snippet based on your description:


def rps_tournament(programs):
    def rps(p1, p2):
        if p1 == p2: return p1
        if (p1=='R' and p2=='S') or (p1=='P' and p2=='R') or (p1=='S' and p2=='P'): return p1
        return p2
    
    while len(programs) > 1:
        programs = [rps(programs[i], programs[(i+1)%len(programs)]) for i in range(0, len(programs), 2)]
        
    if programs[0] == 'IMPOSSIBLE': return 'IMPOSSIBLE'
    
    program = programs[0] * (10**5//len(program)) + programs[0][:10**5%len(program)]
    for i in range(1, len(program)+1):
        if rps(program[:i], program[i-1:i+2]) == program[i-1:i+2]: return program[:i]
        
    return 'IMPOSSIBLE'

This code uses a recursive function to determine the outcome of each round in the game. The tournament is played until only one robot remains, which could be the winner or loser depending on the initial sequence of moves. If after 10^5 rounds the two robots still have not determined the winner (which means they are playing against themselves), a random guess is made and checked if it leads to victory.