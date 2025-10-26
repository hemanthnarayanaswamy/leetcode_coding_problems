class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = set()

        for s, e in nums:
            for i in range(s,e+1):
                res.add(i)
        
        return len(res)