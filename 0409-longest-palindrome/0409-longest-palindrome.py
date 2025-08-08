class Solution:
    def longestPalindrome(self, s: str) -> int:
        sFreq = Counter(s)
        count = 0
        middle = True

        for _, v in sFreq.items():
            if v % 2:
                if middle: 
                    count += v
                    middle = False
                else:
                    count += v - 1
            else: 
                count += v
        
        return count