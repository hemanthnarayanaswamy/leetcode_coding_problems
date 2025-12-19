class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = []

        for i in range(n):
            pre = len(set(nums[0:i+1]))
            suf = len(set(nums[i+1:]))
            diff.append(pre - suf)
         
        return diff
    