import math

def solution(N, K):
    # Calculate the total exposed surface area of each pancake
    areas = []
    for i in range(N):
        radius = float(input().split()[0])
        height = float(input().split()[1])
        areas.append(math.pi * radius**2 + 2 * math.pi * radius * height)
    
    # Sort the pancakes by descending area
    sorted_areas = sorted(areas, reverse=True)
    
    # Choose the top K pancakes and calculate their total exposed surface area
    chosen_areas = sorted_areas[:K]
    total_area = sum(chosen_areas)
    
    return total_area