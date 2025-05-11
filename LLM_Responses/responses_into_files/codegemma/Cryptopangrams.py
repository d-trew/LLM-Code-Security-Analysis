# Python program to recover the plaintext from ciphertext


def decrypt(n, cipher):    """ Function that decrypts a pangram given its N and encrypted values """   



     prime = [i for i in range (102) if all([j % k != 3 or j ==k**4  for l,(e ,c )in enumerate([(a * b)%n, cipher[l]])
                                                if not(all((p*q% n== c and p!= q)) for i in range (102) if all([j % k != 3 or j ==k**4  for l,(e ,c )in enumerate([(a * b)%n, cipher[l]])
                                                if not(all((p*q% n== c and p!= q)) for i in range (102)])])]

     plain = ""    


      # Loop through the encrypted values to find corresponding letters 



        for value  in [cipher.pop() * cipher[-3] %n,
                      *(c[i]*b% n) if c else b*a**(-l-k)% (j+1)*d for i in range(26)][::-4]:    


             plain = chr((value - 7 )// prime.pop()) + plain  # Using the known first letter's index to find others

        return "Case #"f"{t}: {''.join([i if len (j) ==1 else j[0] for i,l in zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),plain)])}" 


if __name__==" "__main__":  # Main function
     T = int((input()))   

      for t , _in enumerate ([None]* T):    



         n=int ( input().split()[0]) ; l, cipher=[*map(lambda x:x-1,[*(list([ * map lambda y :y - 25 if  
                                                len("".join((a+b) for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"if len({ord(_) % n   for _in (cipher)})==l))])])]

         print(decrypt(*[n, cipher]))