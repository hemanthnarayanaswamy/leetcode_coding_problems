class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # if len(nums) < 3:
        #     return -1
        mi, ma = min(nums), max(nums)

        for num in nums:
            if num != mi and num != ma:
                return num
        
        return -1