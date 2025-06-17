class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arrFreq = Counter(arr)
        result = -1

        for val, freq in arrFreq.items():
            if val == freq:
                if val > result:
                    result = val
        
        return result