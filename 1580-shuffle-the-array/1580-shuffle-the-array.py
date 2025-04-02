class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = [0] * len(nums)
        k = 0
        for i in range(n):
            final[k]  = nums[i]
            k += 2
        k = 1
        for i in range(n,len(nums)):
            final[k] = nums[i]
            k += 2
        return final