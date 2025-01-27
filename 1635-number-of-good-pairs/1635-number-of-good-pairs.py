class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        good_pair_count = 0
        for i in unique_nums:
            n = nums.count(i)
            if n > 1:
                pair_possibilities = n * (n-1) // 2
                good_pair_count += pair_possibilities
        return good_pair_count
        