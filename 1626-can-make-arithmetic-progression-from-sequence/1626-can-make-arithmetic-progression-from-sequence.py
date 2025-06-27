class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arrSorted = sorted(arr)

        diffval = arrSorted[1] - arrSorted[0]

        for i in range(2, len(arrSorted)):
            if arrSorted[i] - arrSorted[i-1] != diffval:
                return False
        
        return True