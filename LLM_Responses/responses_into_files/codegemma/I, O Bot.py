from collections import defaultdict



def calculatePower(N: int , C :int) -> str {    # N - number balls in Io, c- change power cost per ball transformation  ball shape dictionary with key as station and value is list of shapes 

        shapeDict = {} # map from location to set
     for _x,_s   in [list(map ( int , input().split())) for i_loop134 in range((N))]:    # N - number balls, x- position s shape  ball dictionary with key as station and value is list of shapes 

            shapeDict.setdefault(_a,-set()).add (_b)
        power =0 # total power used by BALLE to transfer all beach ball from Io's surface locations into the warehouse   total units are stored in variable named 'Power'.  ball shape dictionary with key as station and value is list of shapes 


     for _x,_y    in [list(map (int,input().split())) for i_loop135] : # N - number balls x- position sshape
        if len(_s) ==2:   # if there are two different ball in one location then we need to change the shape of both 

            power += C*len( _a )  


     return f"Case #{i_loop136}: {int ( power)} " # return total units used by BALLE as a string
    print()



if __name__ == "__main__":   # main function to call calculatePower for each test case

        T = int(input())  


     for i in range(( T)): 




            N,C= map (int , input().split ()) # N - number balls c- change power cost per ball transformation
    print()