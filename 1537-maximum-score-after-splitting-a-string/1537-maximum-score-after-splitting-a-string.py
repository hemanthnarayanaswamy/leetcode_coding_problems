class Solution:
    def maxScore(self, s: str) -> int:
        sum = 0
        left_sum, right_sum = 0, 0
        for i in range(1,len(s)):
            left_sum =  s[:i].count('0')
            right_sum = s[i:].count('1')
            sum = max(sum, left_sum + right_sum)
            
        return sum