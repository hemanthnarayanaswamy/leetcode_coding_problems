from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []
        
        # 1) Place everything in the order of arr2
        for x in arr2:
            c = freq.pop(x, 0)
            result.extend([x] * c)
        
        # 2) Sort whatever remains in freq and append
        leftovers = dict(sorted(freq.items(), key=lambda x:x[0]))
        
        for n, f in leftovers.items():
            result.extend([n] * f)
        
        return result