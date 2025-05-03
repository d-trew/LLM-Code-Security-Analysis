import sys

def main():
    T = int(input())
    
    for i in range(1, T+1):
        S = input()
        
        max_score = 0
        last_requested = None
        coding_points = 0
        jamming_points = 0
        
        for day, mood in enumerate(S):
            if mood == 'C':
                if last_requested is None or last_requested == 'J':
                    max_score += 10
                    coding_points += 5
                else:
                    coding_points = 5
            
            elif mood == 'J':
                if last_requested is None or last_requested == 'C':
                    max_score += 5
                    jamming_points += 10
                else:
                    jamming_points = 5
            
            last_requested = mood
        
        print("Case #{}: {}".format(i, max_score + coding_points - jamming_points))
    
if __name__ == "__main__":
    main()