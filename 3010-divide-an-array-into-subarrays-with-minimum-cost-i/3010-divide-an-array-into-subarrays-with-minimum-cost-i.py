class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minCost = nums[0]
        newNums = nums[1:]
        newNums.sort()

        minCost += newNums[0] + newNums[1]

        return minCost
