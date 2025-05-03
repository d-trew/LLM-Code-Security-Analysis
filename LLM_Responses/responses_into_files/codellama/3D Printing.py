import math

def main():
    T = int(input())
    for t in range(T):
        C_i, M_i, Y_i, K_i = map(int, input().split())
        # Find the maximum amount of ink that can be used from each color
        maxC = min(10**6, C_i)
        maxM = min(10**6, M_i)
        maxY = min(10**6, Y_i)
        maxK = min(10**6, K_i)
        
        # Calculate the minimum amount of ink required for each color
        minC = math.floor((10**6 - maxM - maxY - maxK) / 4)
        minM = math.floor((10**6 - maxC - maxY - maxK) / 4)
        minY = math.floor((10**6 - maxC - maxM - maxK) / 4)
        minK = math.floor((10**6 - maxC - maxM - maxY) / 4)
        
        # Check if there is enough ink to print the D's
        if maxC < minC or maxM < minM or maxY < minY or maxK < minK:
            print("IMPOSSIBLE")
        else:
            print(f"Case #{t+1}: {minC} {minM} {minY} {minK}")

if __name__ == "__main__":
    main()