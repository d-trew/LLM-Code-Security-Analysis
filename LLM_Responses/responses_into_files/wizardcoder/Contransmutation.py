import sys
from math import inf

def main():
    T = int(input())
    
    for i in range(1, T+1):
        M, G = map(int, input().split())
        
        formulas = [list(map(int, input().split())) for _ in range(M)]
        lead_grams = 0
        
        while True:
            max_lead_formula = -1
            max_metal = None
            
            for metal in range(2, M+1):
                formula = formulas[metal-1]
                
                if len(set(formula)) == 2 and formula.index(metal) != 0:
                    metal_to_lead = formula.index(1)
                    
                    if formula[metal_to_lead] > max_lead_formula:
                        max_lead_formula = metal_to_lead
                        max_metal = metal
            
            if not max_metal:
                break
            
            grams_of_max_metal = G[max_metal-1]
            if grams_of_max_metal == 0:
                break
            
            formulas.pop(max_metal-1)
            G[1-1] += max_lead_formula * grams_of_max_metal
            G[max_metal-1] = 0
        
        lead_grams += sum([G[0]] + [x for x in G if x > 0])
        
        print(f"Case #{i}: {lead_grams % (10**6+7)}")

if __name__ == "__main__":
    main()