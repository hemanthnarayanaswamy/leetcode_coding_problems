class Solution:
    def minElement(self, nums: List[int]) -> int:
        digitSum = []

        for num in nums:
            digitSum.append(sum([int(n) for n in str(num)]))
        
        return min(digitSum)
