def fractal_artwork(K, C, S):
    # Initialize a list to store the positions of the tiles to clean
    tiles = []

    # Check if it is possible to determine whether there is at least one G tile in the artwork
    if C == 1:
        # If the complexity is 1, then the answer is trivially yes
        return "IMPOSSIBLE"
    elif C == 2:
        # If the complexity is 2, then there must be at least one G tile in the artwork
        return "1 2"
    else:
        # Otherwise, check if it is possible to determine whether there is at least one G tile in the artwork by cleaning a subset of tiles
        for i in range(S):
            # Check if the current tile is a G tile
            if K[i] == "G":
                # If the current tile is a G tile, then add its position to the list of tiles to clean
                tiles.append(str(i+1))
        if len(tiles) > 0:
            # If there are any G tiles in the subset of tiles to clean, then return their positions
            return "Case #" + str(C-1) + ": " + " ".join(tiles)
        else:
            # If there are no G tiles in the subset of tiles to clean, then the answer is trivially no
            return "IMPOSSIBLE"