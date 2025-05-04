def dragonVsKnight(Hd , Ad   =10**3):     # Initialize health and attack power for both the Dragon (D)and Knight K respectively        Hkd = Hk ; Akd  , Brd      \                  ## copy values of input parameters from function arguments to local variables
                                                         Adu    Bdr          

            while True:                 ### Loop until one character is defeated. 


                if Hd <=0 :             # if Dragon health falls below zero then it loses and game over!        return "IMPOSSIBLE"  ## return impossible as dragon lost the battle   



               elif Hk<=1 or (Hkd - Adu * Brd + Akd) >=Hd: # If knight's attack is stronger than dragons defense, he wins.
                    if(Bdr > 0):         # if there are buffs active on Dragon then remove them as they do not help against strong opponent    ## removing buff from dragon to counter the knights strength increase  

                        Hkd -= Adu * Brd - Akd   ### calculate new health of knight with all debuffs and attack power reduction
                    else:                 #### no need for any buffs, just reduce dragons life by attackers damage 


                            Hd-=AkD        ## reducing Dragon's Health to combat the knights Attack  

                elif Hk <=0 :          # If Knight is defeated then dragon wins. Game over!      return str(turn)   ### return turn counter as it shows how many turns took for dragons victory
                 else: 


                    if Bdr > Akd * Drd - Adu +1 or (Hkd-AkD*Bdk+Adu)<Hd :  ## checking if buff is enough to protect dragon from next attack of knight and also increase its health

                        turn +=3          ### increment turn counter by three as it takes 2 turns for debuffing opponent followed with two more actions(attack, cure)
                    else:                 #### no need any buffs just reduce the dragons life based on attackers damage  


                            Hd -= AkD        ## reducing Dragon's Health to combat opponents Attack