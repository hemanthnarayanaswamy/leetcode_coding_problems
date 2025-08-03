class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = [i for i, v in enumerate(nums) if v == 1]
        
        return all(j - i > k for i, j in zip(ones, ones[1:]))