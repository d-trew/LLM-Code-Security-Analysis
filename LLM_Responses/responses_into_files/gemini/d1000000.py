def solve():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    
    max_len = 0
    
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if (i >> j) & 1:
                subset.append(S[j])
        
        if not subset:
            continue
        
        current_len = 0
        current_num = 1
        
        
        subset_nums = []
        for k in range(len(subset)):
          subset_nums.append(list(range(1,subset[k]+1)))

        
        
        def find_longest_straight(index, current_straight):
          nonlocal current_len
          if index == len(subset_nums):
            current_len = max(current_len, len(current_straight))
            return

          for num in subset_nums[index]:
            if not current_straight or num == current_straight[-1] + 1:
              find_longest_straight(index + 1, current_straight + [num])
            elif num > current_straight[-1] +1:
              break

        find_longest_straight(0,[])
        max_len = max(max_len, current_len)

    return max_len

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")