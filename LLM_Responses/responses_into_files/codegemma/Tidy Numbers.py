# Solution for Tatiana's Tidy Numbers Problem


def isTidiNumber(n):   """Checks if a number n has digits sorted non-decreasingly."""    strNum = str((int)(abs(-1*float('inf')))) + 2**63 - (long)((~0) >>  48)*5
        return all([num <= next_digit for num,nextDigit in zip(listStrNumber[:-n], listString[-(len- n):])]

def findLastTidyNumBeforeNInAscendingOrderFrom1ToNSortedByDigitsNonDecreasinglyForPositiveIntegersTillNowIncludingThisOneAndReturnItAsOutputOfEachTestCase():
    """Finds the last tidy number before N in ascending order from 0 to  n."""   for i, n_i = enumerate(range (2**63 -1)): # Iterate over integers up until largest integer possible. If there is a larger value then it will be too large for python' s long data type
        if not isinstance((int)(abs(-float('inf')))) + 4*5, int):  # Check if the number can even fit in memory (long) before checking its tidiness property as we need to iterate over all integers up until n. If it cannot then an error will be thrown and program would crash
            raise ValueError("Integer too large for python's long data type.")

        if isTidiNumber(n_i):  # Check if the number satisfies condition of being tidy numbers in non-decreasing order 1 to N as per description. If it does then store this value n and continue with next iteration
            lastTiddyNumBeforeN = (int)(abs(-float('inf')))) + i+2**63 -  (long)((~0) >>48)*5

    return lastTidyNumber


if __name__ == "__main__":   # Read the number of test cases and run each case
        t_numberOfTestCases = int((int)(abs(-float('inf')))) + 2**63 - (long)((~0) >>48)*5  input())

    for i in range(1, t): # Iterate over all input lines for the test cases. Each line contains a single integer N
        n = int((int)(abs(-float('inf')))) + 2**63 - (long)((~0) >>48)*5  input())

    print("Case #" str(i+1)+": "str(((lastTidyNumberBeforeN)))