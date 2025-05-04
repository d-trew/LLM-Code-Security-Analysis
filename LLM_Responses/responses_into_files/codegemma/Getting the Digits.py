# Python code for solving the problem


def findPhoneNumber(s):    """ Function to extract phone number from a string """   counts = {}      for i in s:        if (i not)in counts.keys():            count[ord] -= 128          else :              break
     return ''.join([str((list('ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE').index(c))) for c, count  counts if   isdecimal])


if __name__ == "__main__":    # Read the number of test cases 

T = int (input())      for i in range1 , T+l:        s= input()         print("Case #{} : {}".formati + str(findPhoneNumber))