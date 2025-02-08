def solve():
    AC, AJ = map(int, input().split())
    cameron_activities = []
    for _ in range(AC):
        cameron_activities.append(list(map(int, input().split())))
    jamie_activities = []
    for _ in range(AJ):
        jamie_activities.append(list(map(int, input().split())))

    cameron_total_time = sum(d - c for c, d in cameron_activities)
    jamie_total_time = sum(k - j for j, k in jamie_activities)

    
    def count_exchanges(schedule):
        exchanges = 0
        current_person = 'cameron' if schedule[0][0] == 0 else 'jamie'
        
        intervals = sorted(schedule)
        
        last_time = 0
        for start, end in intervals:
            if start > last_time and current_person == 'cameron':
                exchanges +=1
                current_person = 'jamie'
            elif start > last_time and current_person == 'jamie':
                exchanges +=1
                current_person = 'cameron'
            last_time = end

        return exchanges

    
    best_schedule = []
    min_exchanges = float('inf')


    
    def generate_schedules(current_schedule, remaining_cameron, remaining_jamie, current_person):
        nonlocal best_schedule, min_exchanges

        if not remaining_cameron and not remaining_jamie:
            schedule = sorted(current_schedule)
            exchanges = count_exchanges(schedule)
            if exchanges < min_exchanges:
                min_exchanges = exchanges
                best_schedule = schedule
            return

        if remaining_cameron:
            generate_schedules(current_schedule + remaining_cameron[:1], remaining_cameron[1:], remaining_jamie, 'cameron')

        if remaining_jamie:
            generate_schedules(current_schedule + remaining_jamie[:1], remaining_cameron, remaining_jamie[1:], 'jamie')
        
    cameron_intervals = []
    for c,d in cameron_activities:
        cameron_intervals.append((c,d))
    jamie_intervals = []
    for j,k in jamie_activities:
        jamie_intervals.append((j,k))
    
    generate_schedules([], cameron_intervals, jamie_intervals,'')
    

    return min_exchanges


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")