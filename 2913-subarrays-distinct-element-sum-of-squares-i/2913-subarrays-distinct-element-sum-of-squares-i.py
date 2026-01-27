class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            distinct = set()
            l = 0
            for j in range(i, n):
                if nums[j] not in distinct:
                    distinct.add(nums[j])
                    l += 1
                count += l**2
        
        return count
        