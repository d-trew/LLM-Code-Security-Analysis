def reversort(lst):
    n = len(lst)
    total_cost = 0
    
    for i in range(n-1):
        j = lst.index(min(lst[i:]), i) + 1
        sublist_length = j - i
        
        # Reverse the sublist and add its length to total cost
        total_cost += sublist_length 
        
        lst[i:j] = reversed(lst[i:j])
    
    return total_cost

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    cost = reversort(lst)
    
    print('Case #{}: {}'.format(case, cost))