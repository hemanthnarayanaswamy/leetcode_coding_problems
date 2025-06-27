class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # 1) Sort in-place
        nums.sort()
        n = len(nums)
        
        # 2) Find leftmost index where nums[idx] == target (lower_bound)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        left = lo
        
        # If out of bounds or not actually target, no occurrences
        if left == n or nums[left] != target:
            return []
        
        # 3) Find first index > target (upper_bound)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        right = lo
        
        # 4) All indices in [left, right) are equal to target
        return list(range(left, right))
