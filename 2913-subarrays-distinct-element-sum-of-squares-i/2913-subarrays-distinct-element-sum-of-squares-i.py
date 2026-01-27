class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            distinct = set()
            l = 0  # To track lenght instead of re calculating everytime
            for j in range(i, n):
                if nums[j] not in distinct:
                    distinct.add(nums[j])
                    l += 1
                count += l*l
        
        return count
