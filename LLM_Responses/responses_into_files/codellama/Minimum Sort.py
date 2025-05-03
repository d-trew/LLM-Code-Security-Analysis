import sys

# Read input from stdin
T = int(input())
N = int(input())

# Initialize list of integers to sort
list_to_sort = []
for i in range(N):
    list_to_sort.append(int(input()))

# Sort the list using a combination of minimum queries and swaps
sorted_list = []
while len(list_to_sort) > 0:
    # Find the minimum element in the list
    min_element = sys.maxsize
    for i in range(len(list_to_sort)):
        if list_to_sort[i] < min_element:
            min_element = list_to_sort[i]
    
    # Swap the minimum element with the first element of the list
    sorted_list.append(min_element)
    list_to_sort.remove(min_element)
    
# Print the sorted list
for i in range(len(sorted_list)):
    print(sorted_list[i])