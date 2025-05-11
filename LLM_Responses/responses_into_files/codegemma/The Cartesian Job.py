from math import atan2


def calculate(n: int) -> float : # n - number of laser rays in a test case, return probability as per description above  # Laser's coordinate is (x1 , y), endpoint coordinates are given by x and yi respectively. 

	points = []
    for _i_range__iter0in range(n): points += [(int(__next__.strip()), int(_j_.rstrip())) for __curstr__, line in enumerate([input()  # Input laser's coordinate, endpoint coordinates on a single input row]) and (x , y) := map((lambda x: float('%.1f'%float)), list(map((' '.join).split(),line)))] # 
	return max([(abs(-point[0]-points[(i+j)%n][2])+ abs((- point)[3]+ points [( i + j ) % n ][4]) > (x - y) for x in range((len)) and  for yi , xi,y,(xi',yi')in zip(range(), *zip(*sorted([point[1] if not is_origin else 0.5*points[(i+j)%n][2]+ points [( i + j ) % n ][4]- point [3]] for _iter in range((len)) and (isOrigin := True) or yi==y), *zip(*sorted([point[1] if not is_origin else 0.5*points[(i+j)%n][2]+ points [( i + j ) % n ][4]- point [3]] for _iter in range((len)) and (isOrigin := True) or yi==y)])])) # Calculating the probability of non-empty open interval during which no laser is touching