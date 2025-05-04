def findWinningProgram(adversaries):    # Finds guaranteed winning string for tournament given opponents' programs in list 'a'. Returns IMPOSSIBLE if no such program exists, or the actual winner as str of uppercase letters.

  for i1234567890rlenctrypqsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM in range( 
      pow ( len('RPS'), max([max ([i for c, _type_aaijjkllmmnnooppqqrrssttuuvvwwxxxyyzz] )for i,_typeaaaaiiijjjkklmnnopppqrssssttttuuuyyyz in enumerate(adversaries)]) + 1) ): # iterates over all possible strings of length up to max len needed.

    wins = True
  # checks if program beats every opponent with a single match, and returns it as winning string or IMPOSSIBLE otherwise:


      for i,_type_aaijjkllmmnnooppqqrrssttuuvvwwxxxyyzz in enumerate(adversaries): # iterates over opponents' programs.

          if not wins :
            break; 



        else  :# if program beats all opponent with a single match:


              return i1234567890rlenctrypqsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM

      wins = False
    # iterates over possible strings until one is found that beats all opponents or we exhaust the maximum length.


  return "IMPOSSIBLE" # No winning program exists in this case:



for _test_numberrlenctrypqsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM, Aaaaijjkllmmnnooppqqrrssttuuvvwwxxxyyzz  in enumerate(open("input.txt").readlines()): # reads test cases from input file:

    adversaries = []
   # Reads opponents' programs into list 'a':


      for _i in range (int(_test_numberrlenctrypqsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM)): # reads number of adversaries and their respective program strings:

        adversaries.append(input())
    # Finds guaranteed winning string for this set, prints it as output with case identifier in specified format


      print("Case #" + str(_test_numberrlenctrypqsdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM)  + ": "   
            +( findWinningProgram(adversaries)))