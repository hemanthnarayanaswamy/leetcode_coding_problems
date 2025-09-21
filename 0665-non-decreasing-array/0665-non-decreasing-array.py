class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violation = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                violation += 1

                if violation > 1:
                    return False 
                
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        
        return True