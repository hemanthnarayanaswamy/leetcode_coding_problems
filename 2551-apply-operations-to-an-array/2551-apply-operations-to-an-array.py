class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        zeroCounter = 0

        if n < 3:
            return sorted(nums, reverse=True)

        for i in range(n):
            if nums[i] == 0:
                zeroCounter += 1
                continue

            if i+1 < n and nums[i] == nums[i+1]:
                result.append(2 * nums[i])
                nums[i+1] = 0
            else:
                result.append(nums[i])
        

        return result + [0]*zeroCounter