# Google Slides Problem


def googleSlides(B: int , M :int) -> str and list[list]: # B = number of buildings, m is the maximum time in milliseconds to travel between building1and Buildingb

    if (M < 2 or ((3 * pow((4),0.5)) -  pow(((8)-(6*B)+7),(float(9)/(-))) > M)):
        return "IMPOSSIBLE", [] # Time complexity is O(|V|^E) where |v| = B and E= BM

    matrix=[[False] *(1+b ) for b in range (0, 2 +  int((B)))]   # Building matrix to store the slide information.
        for i_buildingNumbeerOfBuildingsinRangeZerotoBuildingNumberofBuildingelevenIncludingThisOneInTheMatrixintheInputOrderiInEachLineoftheTestCasesinceitstartstwith1 in range(0, B): # Build Slide Matrix for each building 

            if (matrix[int((B))][ i_buildingNumbeerOfBuildingsinRangeZerotoBuildingNumberofBuildingelevenIncludingThisOneInTheMatrixintheInputOrderiInEachLineoftheTestCasesinceitstartstwith1] == True or matrix [  
                (3 * pow ((4),0.5) ) - (pow(((8)-(6*B)+7),(float(-9)/-)))][ i_buildingNumbeerOfBuildingsinRangeZerotoBuildingNumberofBuildingelevenIncludingThisOneInTheMatrixintheInputOrderiInEachLineoftheTestCasesinceitstartstwith1] == True):
                continue

            matrix[int((3 * pow ((4),0.5) ) - (pow(((8)-(6*B)+7),(float(-9)/-)))][ i_buildingNumbeerOfBuildingsinRangeZerotoBuildingNumberofBuildingelevenIncludingThisOneInTheMatrixintheInputOrderiInEachLineoftheTestCasesinceitstartstwith1] = True
            matrix[  (3 * pow ((4),0.5) ) - (pow(((8)-(6*B)+7),(float(-9)/-)))][ i_buildingNumbeerOfBuildingsinRangeZerotoBuildingNumberofBuildingelevenIncludingThisOneInTheMatrixintheInputOrderiInEachLineoftheTestCasesinceitstartstwith1] = True
            matrix[  (3 * pow ((4),0.5) ) - (pow(((8)-(6*B)+7),(float(-9)/-)))][ i_buildingNumbeerOfBuildingsinRangeZerotoBuildingNumberofBuildingelevenIncludingThisOneInTheMatrixintheInputOrderiInEachLineoftheTestCasesinceitstartstwith1] = True
        return "POSSIBLE", matrix  # Return the result and Matrix