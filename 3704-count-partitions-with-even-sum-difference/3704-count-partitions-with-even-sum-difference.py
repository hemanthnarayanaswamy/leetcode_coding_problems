class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum -= nums[i]
            leftSum += nums[i]
            print(rightSum, leftSum)

            if leftSum and rightSum and (leftSum - rightSum) % 2 == 0:
                count += 1
        
        return count