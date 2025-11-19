class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = len(arr1)

        for a1 in arr1:
            for a2 in arr2:
                if abs(a1 - a2) <= d:
                    res -= 1
                    break
        
        return res
