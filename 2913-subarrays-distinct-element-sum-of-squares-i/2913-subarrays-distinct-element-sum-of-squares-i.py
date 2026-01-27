class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            distinct = set()
            l = 0  # To track lenght instead of re calculating everytime
            for c in nums[i:]:
                if c not in distinct:
                    distinct.add(c)
                    l += 1
                count += l*l
        
        return count
