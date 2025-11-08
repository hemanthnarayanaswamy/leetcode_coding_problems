class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = min(nums)
        u = max(nums)
        numsSeach = set(nums)
        res = []

        for i in range(l, u+1):
            if i not in numsSeach:
                res.append(i)
        
        return res
