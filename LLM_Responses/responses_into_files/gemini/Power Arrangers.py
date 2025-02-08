T, F = map(int, input().split())

def solve():
    missing_set = ""
    
    indices_to_check = []
    for i in range(F):
        index_to_check = i +1
        indices_to_check.append(index_to_check)
        print(index_to_check)
        letter = input()

        if letter == 'N':
            return
        
    
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    
    
    for i in range (0,len(indices_to_check)):
        index = indices_to_check[i]
        set_index = (index -1) // 5
        letter_index = (index -1) % 5
        
        if letter_index == 0:
            counts['A'] +=1
        elif letter_index == 1:
            counts['B'] +=1
        elif letter_index == 2:
            counts['C'] +=1
        elif letter_index == 3:
            counts['D'] +=1
        elif letter_index == 4:
            counts['E'] +=1

    
    missing_set_counts = {'A': 24, 'B': 24, 'C': 24, 'D': 24, 'E': 24}
    
    for key in counts:
        missing_set_counts[key] -= counts[key]

    missing_set_str = ""
    for key in missing_set_counts:
      if missing_set_counts[key] == 23:
          missing_set_str += key
          

    print(missing_set_str)
    result = input()
    if result == 'N':
        return


for _ in range(T):
    solve()