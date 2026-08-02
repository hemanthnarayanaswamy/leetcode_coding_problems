class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        strength = 0

        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]

                g = math.gcd(a, b)

                tmp = (a * b) // g**2

                if tmp > strength:
                    strength = tmp
        
        return strength