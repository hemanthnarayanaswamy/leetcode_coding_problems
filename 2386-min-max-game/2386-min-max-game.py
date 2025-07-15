class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            newNums = []
            count = 0
            for i in range(0, len(nums), 2):
                if count % 2 == 0:
                    newNums.append(min(nums[i], nums[i + 1]))
                else:
                    newNums.append(max(nums[i], nums[i + 1]))
                count += 1
            nums = newNums
            
        return nums[0]