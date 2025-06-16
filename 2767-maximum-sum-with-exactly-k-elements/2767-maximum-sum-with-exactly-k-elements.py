class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
       z = 2*max(nums)-1+k
       return z * k //2
