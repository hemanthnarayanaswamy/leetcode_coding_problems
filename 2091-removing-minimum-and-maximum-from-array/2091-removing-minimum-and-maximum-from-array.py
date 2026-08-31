class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi, ma = min(nums), max(nums)
        n = len(nums)

        i1 = nums.index(mi)
        i2 = nums.index(ma)
        
        c1 = max(i1, i2) + 1
        c2 = n - min(i1, i2)
        c3 = min(i1, i2) + 1 + n - max(i1, i2)

        return min(c1, c2, c3)


        
