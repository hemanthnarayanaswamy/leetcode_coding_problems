class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = 0, 0

        for num in nums:
            num = abs(num)
            if num > m1:
                m1, m2 = num, m1
            elif num > m2:
                m2 = num
        
        res = 10**5 * m1 * m2

        return res if res > 0 else -res