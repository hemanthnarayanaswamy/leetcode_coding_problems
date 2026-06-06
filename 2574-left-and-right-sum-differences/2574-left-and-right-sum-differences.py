class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = sum(nums)
        n = len(nums)
        ans = []

        for i in range(n):
            rightSum -= nums[i]
            ans.append(abs(leftSum - rightSum))
            leftSum += nums[i]
        
        return ans

        