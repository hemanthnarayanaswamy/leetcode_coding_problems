class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start = min(nums)
        end = max(nums)

        ref = set(nums)
        res = []

        for num in range(start+1, end):
            if num not in ref:
                res.append(num)
        
        return res