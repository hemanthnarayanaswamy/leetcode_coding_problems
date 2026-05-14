class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        groups = 1 # Atleast we'll have one subsequence
        nums.sort()
        numMin = nums[0]

        for num in nums:
            if num - numMin > k:
                groups += 1
                numMin = num
        
        return groups
