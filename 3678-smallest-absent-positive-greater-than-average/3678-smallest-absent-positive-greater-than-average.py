class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        num = max(1, floor(avg) + 1) #Instead of using the int, floor the avg and add 1
        numsPresent = set(nums) # if num is negative we are resetting its start value to 1
        
        while num in numsPresent:
            num += 1
        
        return num
            