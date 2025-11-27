class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        pivotIdx = False
        shifts = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                if pivotIdx:
                    return -1
                else:
                    pivotIdx = True 
                    shifts = n - i - 1
        
        return shifts
