class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        i1 = nums.index(min(nums))
        i2 = nums.index(max(nums))
        
        c1 = max(i1, i2) + 1 # operations to delete from front
        c2 = n - min(i1, i2) # operations to delete from back
        c3 = min(i1, i2) + 1 + n - max(i1, i2) # operation to delete from both sides

        return min(c1, c2, c3)


        
