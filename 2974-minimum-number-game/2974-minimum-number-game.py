class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        res = []

        while nums:
            p1 = nums.pop()
            p2 = nums.pop()
            res.append(p2)
            res.append(p1)
        
        return res