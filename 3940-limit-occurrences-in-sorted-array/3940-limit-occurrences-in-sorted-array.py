class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = dict(Counter(nums).items())
        res = []

        for num,val in freq.items():
            if val >= k:
                res.extend([num]*k)
            else:
                res.extend([num]*val)
        
        return res