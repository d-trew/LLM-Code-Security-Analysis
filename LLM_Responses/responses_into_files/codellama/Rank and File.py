import sys

def get_missing_list(lists):
    # Get the number of rows and columns from the input
    num_rows = len(lists) // 2
    num_cols = len(lists[0]) - 1

    # Initialize a dictionary to store the heights of each row and column
    heights = {}
    for i in range(num_rows):
        heights[i] = []
    for j in range(num_cols):
        heights[j] = []

    # Fill the dictionary with the heights from the input lists
    for i in range(num_rows):
        for j in range(num_cols):
            heights[i].append(lists[i * 2 + 1][j])
    for j in range(num_cols):
        for i in range(num_rows):
            heights[j].append(lists[i * 2 + 1][j + num_rows])

    # Find the unique height in each row and column that is not present in the other rows and columns
    missing_list = []
    for i in range(num_rows):
        for j in range(num_cols):
            if len(heights[i]) > 1:
                height = heights[i][0]
                for k in range(1, len(heights[i])):
                    if heights[i][k] != height:
                        missing_list.append(heights[i][k])
    for j in range(num_cols):
        for i in range(num_rows):
            if len(heights[j]) > 1:
                height = heights[j][0]
                for k in range(1, len(heights[j])):
                    if heights[j][k] != height:
                        missing_list.append(heights[j][k])

    # Return the list of unique heights that are not present in both rows and columns
    return missing_list

# Read input
num_cases = int(input())
for case in range(num_cases):
    num_rows = int(input())
    lists = []
    for i in range(2 * num_rows - 1):
        lists.append([int(x) for x in input().split()])

    # Get the missing list
    missing_list = get_missing_list(lists)

    # Output the case number and the missing list
    print("Case #" + str(case + 1) + ": " + str(missing_list))