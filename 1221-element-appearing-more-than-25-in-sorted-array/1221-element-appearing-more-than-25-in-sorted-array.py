class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        maxLen = len(arr) // 4

        arrFreq = Counter(arr)

        for num, count in arrFreq.items():
            if count > maxLen:
                return num 
        