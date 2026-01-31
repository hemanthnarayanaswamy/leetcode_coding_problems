class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res = prev = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] != prev + 1:
                break
            res += nums[i]
            prev = nums[i]

        numsSearch = set(nums)

        while res in numsSearch:
            res += 1
        
        return res
