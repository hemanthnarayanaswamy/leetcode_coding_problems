class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return 1
            
        total = sum(nums)
        avg = total / len(nums)
        num = floor(avg) + 1 # Instead of using the int, floor the avg and add 1

        if num <= 0:
            num = 1

        numsPresent = set(nums)
        
        while num in numsPresent:
            num += 1
        
        return num
            