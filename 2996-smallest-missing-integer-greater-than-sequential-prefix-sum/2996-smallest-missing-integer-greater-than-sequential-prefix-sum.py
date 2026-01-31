class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = prev = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] == prev + 1:
                total += nums[i]
                prev = nums[i]
            else:
                break
        
        numsSearch = set(nums)
        res = total

        while res in numsSearch:
            res += 1
        
        return res
