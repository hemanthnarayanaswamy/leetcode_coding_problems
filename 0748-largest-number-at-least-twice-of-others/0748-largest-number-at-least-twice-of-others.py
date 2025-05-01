class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        idx = nums.index(maxNum)

        for num in nums:
            if num != maxNum and num*2 > maxNum:
                return -1
        
        return idx

        