import sys

def is_valid(n, r, o, y, g, b, v):
    if n < 2 or (r+o+y+g+b+v) != n:
        return False
    if r == 0 and (o > 0 or y > 0 or g > 0 or b > 0 or v > 0):
        return False
    if o == 1 and (r > 0 or y > 0 or g > 0 or b > 0 or v > 0):
        return False
    if y == 1 and (r > 0 or o > 0 or g > 0 or b > 0 or v > 0):
        return False
    if g == 1 and (r > 0 or o > 0 or y > 0 or b > 0 or v > 0):
        return False
    if b == 1 and (r > 0 or o > 0 or y > 0 or g > 0 or v > 0):
        return False
    if v == 1 and (r > 0 or o > 0 or y > 0 or g > 0 or b > 0):
        return False
    
    if r > 2:
        return False
    if o > 2:
        return False
    if y > 2:
        return False
    if g > 2:
        return False
    if b > 2:
        return False
    if v > 2:
        return False
    
    if r == 1 and o > 0 and (o+y) % 2 != 0:
        return False
    if y == 1 and g > 0 and (g+b) % 2 != 0:
        return False
    if g == 1 and b > 0 and (r+b) % 2 != 0:
        return False
    if b == 1 and v > 0 and (v+o) % 2 != 0:
        return False
    
    if r == 1 and o == 1 and y > 0 and g > 0:
        return False
    if y == 1 and g == 1 and b > 0:
        return False
    if g == 1 and b == 1 and v > 0:
        return False
    
    if r == o == 1 and (y+g) % 2 != 0:
        return False
    if y == g == 1 and b > 0:
        return False
    if g == b == 1 and v > 0:
        return False
    
    return True

def place_unicorns(n, r, o, y, g, b, v):
    if not is_valid(n, r, o, y, g, b, v):
        print("IMPOSSIBLE")
        return
    
    for i in range(2**n-1): # iterate through all possible placements of unicorns
        arrangement = bin(i)[2:].zfill(n) # convert to binary and pad with leading zeros if necessary
        
        valid = True
        for j in range(n):
            if (arrangement[j] == '1' and (j-1 >= 0 and arrangement[j-1] != '1') and (j+1 < n and arrangement[j+1] != '1'): # check for red unicorns
                if r > 0:
                    r -= 1
                elif o > 0:
                    o -= 1
                else:
                    valid = False
                    break
            elif (arrangement[j] == '2' and (j-1 >= 0 and arrangement[(j-1)%n] != '2') and (j+1 < n and arrangement[(j+1)%n] != '2'): # check for orange unicorns
                if o > 0:
                    o -= 1
                elif y > 0:
                    y -= 1
                else:
                    valid = False
                    break
            elif (arrangement[j] == '3' and (j-1 >= 0 and arrangement[(j-1)%n] != '3') and (j+1 < n and arrangement[(j+1)%n] != '3'): # check for yellow unicorns
                if y > 0:
                    y -= 1
                elif g > 0:
                    g -= 1
                else:
                    valid = False
                    break
            elif (arrangement[j] == '4' and (j-1 >= 0 and arrangement[(j-1)%n] != '4') and (j+1 < n and arrangement[(j+1)%n] != '4'): # check for green unicorns
                if g > 0:
                    g -= 1
                elif b > 0:
                    b -= 1
                else:
                    valid = False
                    break
            elif (arrangement[j] == '5' and (j-1 >= 0 and arrangement[(j-1)%n] != '5') and (j+1 < n and arrangement[(j+1)%n] != '5'): # check for blue unicorns
                if b > 0:
                    b -= 1
                elif v > 0:
                    v -= 1
                else:
                    valid = False
                    break
            elif (arrangement[j] == '6' and (j-1 >= 0 and arrangement[(j-1)%n] != '6') and (j+1 < n and arrangement[(j+1)%n] != '6'): # check for violet unicorns
                if v > 0:
                    v -= 1
                else:
                    valid = False
                    break
        
        if valid:
            print(arrangement.replace('1', 'R').replace('2', 'O').replace('3', 'Y').replace('4', 'G').replace('5', 'B').replace('6', 'V')) # replace binary digits with unicorn types
            break
    
if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        n, r, o, y, g, b, v = map(int, input().split())
        print("Case #{}: ".format(i), end="")
        place_unicorns(n, r, o, y, g, b, v)