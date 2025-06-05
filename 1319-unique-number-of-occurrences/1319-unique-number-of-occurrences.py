class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrFreq = Counter(arr)
        uniqueCount = set()

        for val in arrFreq.values():
            if val in uniqueCount:
                return False 
            
            uniqueCount.add(val)
        
        return True