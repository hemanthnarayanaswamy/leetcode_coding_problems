class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        if arr == brr:
            return 0
        
        c1 = sum([abs(a-b) for a,b in zip(arr, brr)])
    
        sortedArr = sorted(arr)
        sortedBrr = sorted(brr)

        c2 = sum([abs(a-b) for a,b in zip(sortedArr, sortedBrr)])
        c2 += k

        return min(c1, c2)
