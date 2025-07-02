class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            minNum = min(nums)
            for i in range(len(nums)):
                if nums[i] == minNum:
                    nums[i] *= multiplier
                    break
            k -= 1
        
        return nums
