import math

def largest_valid_set(road_signs):
    max_num_of_signs = 0
    num_of_sets = 0
    for i in range(len(road_signs)):
        if road_signs[i][2] - road_signs[i][1] > max_num_of_signs:
            max_num_of_signs = road_signs[i][2] - road_signs[i][1]
            num_of_sets += 1
    return (max_num_of_signs, num_of_sets)

def solution(road_signs):
    max_num_of_signs = 0
    num_of_sets = 0
    for i in range(len(road_signs)):
        if road_signs[i][2] - road_signs[i][1] > max_num_of_signs:
            max_num_of_signs = road_signs[i][2] - road_signs[i][1]
            num_of_sets += 1
    return (max_num_of_signs, num_of_sets)