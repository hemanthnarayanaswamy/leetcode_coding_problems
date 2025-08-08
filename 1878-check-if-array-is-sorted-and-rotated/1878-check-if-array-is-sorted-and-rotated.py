class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = False 

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                if rotated:
                    return False
                else: 
                    rotated = True
        
        return True
