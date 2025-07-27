class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        maxLen = 0.25 * len(arr)

        arrFreq = Counter(arr)

        for num, count in arrFreq.items():
            if count > maxLen:
                return num 
        