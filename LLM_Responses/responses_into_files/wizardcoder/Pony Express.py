import math
def pony_express(N, routes, horses):
    def horse_time(distance, speed):
        return distance / speed
    
    def travel_time(route, horses):
        total_time = 0
        current_city = 1
        for i in range(len(route)):
            next_city = route[i]
            if next_city == -1:
                break
            total_distance = horse_time(routes[current_city][next_city], horses[current_city])
            current_city = next_city
        return total_distance
    
    def min_travel_time(route, horses):
        if len(route) == 1:
            return 0
        
        result = float('inf')
        for i in range(len(route)):
            if route[i] != -1:
                new_route = [x for x in route]
                new_route.pop(i)
                current_time = travel_time(new_route, horses) + horse_time(routes[current_city][route[i]], horses[current_city])
                if i == 0:
                    current_horse = route[i]
                else:
                    new_horses = [x for x in horses]
                    new_horses[current_city] -= routes[current_city][route[i]]
                    new_horses[route[i]] += routes[current_city][route[i]]
                    current_horse = route[i]
                travel_time_with_change = horse_time(routes[current_horse][route[-1]], horses[current_horse]) + min_travel_time(new_route, new_horses)
                result = min(result, current_time, travel_time_with_change)
        return result
    
    T = int(input())
    for i in range(1, T+1):
        routes = []
        horses = []
        
        N = int(input())
        for j in range(N):
            route = list(map(int, input().split()))
            routes.append([-1] * (N)
        for k in range(N):
            horse_speed, endurance = map(float, input().split())
            horses.append(endurance / horse_speed)
        
        result = min_travel_time(route, horses)
        print("Case #%d: %.6f" % (i, result))