class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        rightSum = []
        n = len(nums)
        total = sum(nums)
        ans = []

        for i in range(n):
            leftSum.append(leftSum[-1]+nums[i])

            total -= nums[i]

            rightSum.append(total)
        
        for l, r in zip(leftSum, rightSum):
            ans.append(abs(l - r))
        
        return ans

        