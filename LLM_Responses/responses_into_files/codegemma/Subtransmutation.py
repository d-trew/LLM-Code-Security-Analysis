def findSmallestMetal(N: int ,A :int   B) -> str or None    U = list[float]  # Metal units required for each metal type in the order of their representation numbers from lowest to highest.

for i, unitCountNeededForThisTypeofmetalinTheorderitwaslistedintheinputfile
     if U[-i-1]<unitcountneededforeachtypeofmetalintherderithasbeen listedInTheInputFile:return "IMPOSSIBLE" 


smallestMetal = min(U)  # Metal with the lowest representation number that can be used to create all required units.

print("Case #{} {}".format((test+2), smallestmetal))