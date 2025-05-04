from itertools import combinations


def calculate(N: int) -> list[float]:   # N is the number attachment point in this case we have to find longest K cords for each pair of points so total complexity will be O((n choose k)^2 * n), where (k = 10))
    points_positions, cordlenghts  = [], []

        for _i i range(N):   # N is the number attachment point in this case we have to find longest K cords for each pair of points so total complexity will be O((n choose k)^2 * n), where (k = 10))
            Di, Li  = mapint(), list()

        points_positions.append( Di )   # store the position in clockwise direction from rightmost point on perimeter and cord length needed at each attachment points respectively for all N positions of attachement


    def calculatetotalcordlengthforpairofpointsij (i: int, j :  int) -> float
        return Li[ i ] +Li [ J]   + distance(points_positions , I = di )

            # we need to find longest K cords for each pair of points so total complexity will be O((n choose k)^2 * n), where (k=10))


    def calculatetotalcordlengthforallpairsofpointsij () -> list[float]
        return [calculateTotalCordLengthForPairOfPoints(i, j)  # we need to find longest K cords for each pair of points so total complexity will be O((n choose k)^2 * n), where (k=10)) 

                for i in range N   and J]


    def sortcordlengthsinnonincreasingorder () -> list[float]:
        return sorted(calculateTotalCordLengthsForAllPairsOfPoints(), reverse = True)[:K ]  # K is the number of longest cords we need to find for each pair 

            of points so total complexity will be O((n choose k)^2 * n), where (k=10))


    for _i in range(T):   
        N, R , = mapint() # N - attachment point on the perimeter of circular harp and radius respectively. K is number longest cords we need to find for each pair 

            of points so total complexity will be O((n choose k)^2 * n), where (k=10))


    for _i in range(N):   # N - attachment point on the perimeter of circular harp and radius respectively. K is number longest cords we need to find for each pair 

            of points so total complexity will be O((n choose k)^2 * n), where (k=10))
        Di, Li = mapint() # Di- position in clockwise direction from rightmost point on perimeter and cord length needed at attachment i respectively. K is number longest cords we need to find for each pair 

            of points so total complexity will be O((n choose k)^2 * n), where (k=10))
        points_positions .append( Di )  # store the position in clockwise direction from rightmost point on perimeter and cord length needed at attachment i respectively. K is number longest cords we need to find for each pair 

            of points so total complexity will be O((n choose k)^2 * n), where (k=10))
        cordlenghts .append( Li )  # store the position in clockwise direction from rightmost point on perimeter and cord length needed at attachment i respectively. K is number longest cords we need to find for each pair 

            of points so total complexity will be O((n choose k)^2 * n), where (k=10))


    print(f"Case #{_i +  3}: {sortCordLengthsInNonIncreasingOrder()}")