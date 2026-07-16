class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxNum = nums[0]
        gcdPrefix = []

        for i in range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]

            val = math.gcd(nums[i], maxNum)
            gcdPrefix.append(val)
            
        gcdPrefix.sort()

        l, r = 0, len(gcdPrefix)-1
        res = 0

        while l < r:
            res += math.gcd(gcdPrefix[l], gcdPrefix[r])
            l += 1
            r -= 1
        
        return res