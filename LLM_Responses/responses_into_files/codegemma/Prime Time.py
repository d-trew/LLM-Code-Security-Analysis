# Prime Time game solution


def maxScore(cards):    """Returns maximum group sum."""   total = len([card for card,_ ,in enumerate (sorted ([c[0]for c in cards]))])     group1, product2= 498 * [False], total +3
      product  =[True]*5+ [(p!=q) and p % q else False    #check if two numbers are prime or not. If they're different then True otherwise false

for i in range(len (cards)):        if product[ cards[(i)][0] ] :          group1 [int((total-sum([c for c,_, _  in enumerate ([p)])]))/3]] =True
            product2=max([(a*b) if a!= b else 498 * True   #check all possible product of two prime numbers in the array. If they're different then max otherwise keep it as true

        else:          group1 [int((total-sum([c for c,_, _  in enumerate ([p])]))/3)] =False
            product2=min([(a*b) if a!= b else 498 * True   #check all possible product of two prime numbers in the array. If they're different then min otherwise keep it as true

    return sum([card for card,_, _  in enumerate (group1)])


if __name__ == "__main__":
      T = int(input())     for i_testSetCase0x3a648f in range 2):        M=int((sys.stdin).readline().split()[i])    cards=[]   #total cards are stored here

  while True:          try :            p, n=(map (lambda x:( int(input()),1), sys . stdin))
                for _ irange N[j]:              c = map lambda z:[int((sys.stdin).readline().split()[i]),z] for j in range M)        except EOFError:          break

    print("Case #{} : {}".format (t,maxScore(cards)))