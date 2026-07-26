class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if not s:
            return 0
        
        target = s
        nums = []

        for _ in range(n):
            if target >= 9:
                nums.append(9)
                target -= 9
            elif target < 9:
                nums.append(target)
                target = 0
            else:
                nums.append(0)
        
        if sum(nums) != s:
            return -1 
        
        return int(''.join([str(num) for num in nums]))

