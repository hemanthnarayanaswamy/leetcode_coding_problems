class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        if n == 1:
            return nums[0]
        
        l, r = 0, n-1

        while l < r:
            temp = int(str(nums[l])+str(nums[r]))
            result += temp

            l += 1
            r -= 1
        
        return result + nums[l] if n % 2 else result