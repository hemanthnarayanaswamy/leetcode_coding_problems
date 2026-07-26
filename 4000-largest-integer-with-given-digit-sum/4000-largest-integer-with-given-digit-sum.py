class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        target = s
        nums = []
        ans = ''

        for _ in range(n):
            digit = min(target, 9)
            target -= digit
            nums.append(digit)
            ans += str(digit)
        
        if sum(nums) != s:
            return -1 
        
        return int(ans)

