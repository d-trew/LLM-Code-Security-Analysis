for _ in range(int((input()))):  # Test cases loop    R, C , F = map ( int,( input().split() )   ) # Dimensions and costs of operations     currentFloorState= [ list ((x)) for x 	in zip(*[iter([c] * R)]*C)])
desiredFinalPattern=[list((y ))for y in  zip (*[[input()]*(R)][0: C])]

def calculateMinimumCoins( current, desired):    count = sum ( a != b and not all ((a == 'M' or 	b== "G")) for i , j,(
        		   			      x)in enumerate((current), start=1 )for y in zip(*[iter([j] * R)]*C))

print(f"Case #{_ +  + :d}: {count}")    if count % F == 0: print ( f"{int ((Count /F))} flips")
else   	     		      			       				        for i in range((R)): if currentFloorState[i] != desiredFinalPattern [j], "swap"