# Python code starts here


def maxCircle(n, friends):    """   Returns the maximum number of kids in a circle with BFFs next to each other """     visited = set()      circleSize=0

for i range (1 n + 2) :        if not visited andi <= N:            startId  # start id is first unvisted node
                dfs(friends, started_id , friends[started], True )          return circlesize    def dfs