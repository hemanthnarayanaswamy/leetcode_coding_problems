class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2 * nums[i]
                nums[i+1] = 0

        result = [num for num in nums if num != 0]

        while n != len(result):
            result.append(0)

        return result