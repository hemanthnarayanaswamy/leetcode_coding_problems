class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        i1 = nums.index(min(nums))
        i2 = nums.index(max(nums))
        
        if i1 > i2:
            i1, i2 = i2, i1

        return min(i2+1,n-i1,i1+1+n-i2)