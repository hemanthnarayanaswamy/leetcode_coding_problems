class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = sorted(Counter(arr).values())  
        unique_count = len(freq) # total number of unique elements in the array
        
        for f in freq:
            if k >= f:
                k -= f
                unique_count -= 1
            else:
                break
        
        return unique_count
            