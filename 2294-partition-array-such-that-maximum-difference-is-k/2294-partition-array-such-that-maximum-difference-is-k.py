class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subCount = 0
        nums.sort()
        numMin = nums[0]

        for i in range(1, n):
            if nums[i] - numMin > k:
                subCount += 1
                numMin = nums[i]
        
        return subCount + 1
