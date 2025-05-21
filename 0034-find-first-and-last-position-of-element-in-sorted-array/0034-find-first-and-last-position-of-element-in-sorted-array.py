class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] == target:
                result.append(left)
            
            if nums[right] == target:
                result.append(right)
            
            left += 1
            right -= 1
        
        if len(result):
            return [min(result), max(result)]
        else:
            return [-1, -1]