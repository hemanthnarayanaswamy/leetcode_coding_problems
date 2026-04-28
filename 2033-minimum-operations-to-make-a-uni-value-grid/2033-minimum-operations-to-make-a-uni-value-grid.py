class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for nums in grid:
            arr.extend(nums)
        
        arr.sort()
        median = arr[len(arr)//2]
        
        ops = 0
        for num in arr:
            diff = abs(median - num)
            d, m = divmod(diff, x)
            if m != 0:
                return -1
            
            ops += d
        
        return ops
