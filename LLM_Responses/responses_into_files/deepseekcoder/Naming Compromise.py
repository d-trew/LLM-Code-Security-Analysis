def edit_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = list(range(len(s1) + 1))
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1] + [0] * len(s1)
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances[index1 + 1] = distances[index1]
            else:
                newDistances[index1 + 1] = 1 + min(distances[index1], distances[index1 + 1], newDistances[index1])
        distances = newDistances
    return distances[-1]

def compromise_name(c, j):
    if len(j) > len(c):
        c, j = j, c

    min_distance = float('inf')
    best_names = []
    for i in range(len(c)):
        name1 = c[:i] + c[i+1:]
        name2 = j[:i] + j[i+1:]
        distance1 = edit_distance(name1, c) + edit_distance(j, name1)
        distance2 = edit_distance(name2, c) + edit<｜begin▁of▁sentence｜>(j, name2)
        if distance1 < min_distance or (distance1 == min_distance and abs(len(name1)-len(c)) < abs(len(best_names[0])-len(c))):
            min_distance = distance1
            best_names = [name1]
        elif distance1 == min_distance:
            best_names.append(name1)
        if distance2 < min_distance or (distance2 == min_distance and abs(len(name2)-len(c)) < abs(len(best_names[0])-len(c))):
            min_distance = distance2
            best_names = [name2]
        elif distance2 == min_distance:
            best_names.append(name2)
    return best_names

t = int(input().strip())
for i in range(1, t + 1):
    c, j = input().strip().split()
    names = compromise_name(c, j)
    print('Case #{}: {}'.format(i, min(names, key=len)))