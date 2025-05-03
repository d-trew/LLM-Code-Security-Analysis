# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, to install scikit-learn:
#   pip install -U scikit-learn
import numpy as np
from collections import defaultdict

def solve(N, A):
    # Initialize a dictionary to store the number of dancers for each color and material
    dancers = defaultdict(int)
    # Initialize a dictionary to store the number of dancers for each row and column
    rows_cols = defaultdict(int)
    
    # Iterate through the matrix A and update the counters for each color, material, and row/column
    for i in range(N):
        for j in range(N):
            if A[i][j] != 0:
                dancers[(A[i][j])] += 1
                rows_cols[(i, j)] += 1
    
    # Initialize a variable to store the minimum number of dancers whose costumes must be changed
    min_dancers = np.inf
    
    # Iterate through each color and material
    for (color, material) in dancers:
        # Calculate the number of dancers with this color and material
        num_dancers = dancers[(color, material)]
        
        # Iterate through each row and column
        for (row, col) in rows_cols:
            # If there are more than one dancer with this color and material in the same row or column
            if rows_cols[(row, col)] > 1:
                # Update the minimum number of dancers whose costumes must be changed
                min_dancers = min(min_dancers, num_dancers)
    
    return min_dancers