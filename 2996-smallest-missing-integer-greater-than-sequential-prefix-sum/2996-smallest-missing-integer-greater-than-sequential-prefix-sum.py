class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res = prev = nums[0]
        n = len(nums)

        for i in range(1, n):
            num = nums[i]
            if num != prev + 1:
                break
            prev = num
            res += prev

        numsSearch = set(nums)

        while res in numsSearch:
            res += 1
        
        return res
