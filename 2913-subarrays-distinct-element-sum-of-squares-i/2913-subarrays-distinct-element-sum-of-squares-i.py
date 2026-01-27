class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                count += len(distinct)**2
        
        return count