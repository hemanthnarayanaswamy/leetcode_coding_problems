class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = nums[0]
        u = nums[-1]
        numsSeach = set(nums)
        res = []

        for i in range(l, u+1):
            if i not in numsSeach:
                res.append(i)
        
        return res
