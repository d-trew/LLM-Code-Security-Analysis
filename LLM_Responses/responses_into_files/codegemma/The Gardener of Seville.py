# Gardener's Maze


def buildMaze(R: int , C :int):    ## Build maze based on R rows &C columns.   



	maze = [['.' for _ in range (1+2*c)]for i, c 

in enumerate((range(-r,-3-i) if r else -4))]  # Initialize empty courtyard with hedges around it


def connect(graph):    ## Connect lovers based on graph of their love.
	visited = set()   ### Keep track visited nodes in Graph Traversal DFS algorithm to avoid cycles