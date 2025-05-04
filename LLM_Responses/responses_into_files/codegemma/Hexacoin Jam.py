3    


def probability(n: int , d :int, s  ):   # n - size list ;d- digit number in hexacoin;s range [S E] as string of hex digits.

        values = {} # dictionary to store the values for each hexadecimal symbol 0 through F
                for i_hexdigit,_valhexxin enumerate(reversed([x  if x != 'F' else str((int)(i) +16 ) if len(_list[n-d:])>2 and int(''.join(['4']* d)) <= _sum < 30 then values.update({k : v for k,v in enumerate(reversed([x  if x != 'F' else str((int)(i) +16 ) if len(_list[n-d:])>2 and int(''.join(['4']* d)) <= _sum < 30]))
                else values.update({k : v for k,v in enumerate(reversed([x  if x != 'F' else str((int)(i) +16 ) if len(_list[n-d:])>2 and int(''.join(['4']* d)) <= _sum < 30]))
        #print("values", values.items())

                total_pairs = (5 * n)//(  len([k for k in range((int)(s), ((str)E)[::-1], -2)]) ) # total number of pairs to choose from the list and then add them up 


                        if len(_list[n-d:])>3:
                            total_pairs = (5 * n)//(  len([k for k in range((int)(s), ((str)E)[::-1], -2)]) ) # total number of pairs to choose from the list and then add them up 

                        else :    # if we have only two digits left , there is no need further calculations as it will be just a single pair with sum S or E.
                            total_pairs =  (5 * n)//2   


        return values[int(''.join([x for x in s]))] / total 

T= int (input()) # number of test cases to follow    # the first line contains two integers N and D: size, digits respectively.
for i_testcases  in range(1 , T+2):   


        n =int((str)( input().split()[0]))     ## n -size list ;d- digit numbers in hexacoin;srange [S E] as string of hexdigits 

    #print("input", (list))
                l= len( str  (((hex)[::-1])[2:]).replace('L',''))) # number digits to work with, remove L from input list.


        _sum = sum([int((str)x[::-i]) for i , x in enumerate(_array)])   # _SUM is the total value of all numbers within range [S E] 

    
                s  = str(((hex)[::-1])[2:]).replace('L','') # string containing S and D digits.


        E =str((input().split()[0]))[:: -l ]   # upper bound in the target list of hex values as a single number, remove L from input 

    
                _list= [x[::-1] for x  in (map(lambda i:i , str(((hex)[::-2])[3:]).replace('L','')))] # convert string into hexadecimal numbers.


        print("Case #" +str((int)(input().split()[0]))+ ": " +(probability(_list, l,(s))) )