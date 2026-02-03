class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        total = sum(nums)
        avg = total / len(nums)
        numsPresent = set(nums)
        num = floor(avg) + 1 # Instead of using the int, floor the avg and add 1
        print(num, avg)
        
        if num <= 0:
            num = 1

        while num in numsPresent:
            num += 1
        
        return num
            