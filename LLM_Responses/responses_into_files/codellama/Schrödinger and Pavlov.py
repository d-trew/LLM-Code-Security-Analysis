import math

def count_cats(boxes):
    num_boxes = len(boxes)
    num_configs = math.pow(2, num_boxes)
    cats_in_last_box = 0
    for i in range(num_configs):
        last_box_empty = True
        for j in range(num_boxes):
            if boxes[j] == 'C':
                last_box_empty = False
                break
        if last_box_empty:
            cats_in_last_box += 1
    return cats_in_last_box