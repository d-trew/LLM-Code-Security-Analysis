def senate_evac(parties):
    from collections import deque
    
    # Create queues for each party
    parties = [(p, i) for i, p in enumerate(parties)]
    q = deque(sorted(parties))
    
    banned = [-1]*26
    cnt = [0]*26
    ans = []
    
    while len(q[0]) > 0:
        _, party_id = q.popleft()
        
        if all(x <= 0 for x in cnt):
            break
            
        # Ban the current party from being banned again
        ban_party = (cnt[party_id] + 1) % 26
        while banned[ban_party] >= 0:
            banned[ban_party] -= 1
            if banned[ban_party] < 0:
                cnt[chr(ban_party + ord('A'))] -= 1
            ban_party = (ban_party + 1) % 26
        
        # Add the current party back to the queue and increase its count
        q.append((parties[party_id][0]-1, party_id))
        cnt[chr(party_id + ord('A'))] += 1
        
        banned[party_id] = 2
        ans.append(chr(party_id + ord('A')))
    
    return " ".join(ans)

T = int(input().strip())
for t in range(1, T+1):
    N = int(input().strip())
    parties = list(map(int, input().strip().split()))
    print("Case #{}: {}".format(t, senate_evac(parties)))