class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0 
        ones = zeros = 0
        largest = float('inf')
        res = ''

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1
            
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1
            
            if ones == k: 
                while s[left] == '0':
                    left += 1
                curr = right - left + 1
                if curr < largest:
                    res = s[left:right+1]
                    largest = curr
                elif curr == largest:
                    if s[left:right+1] < res:
                        res = s[left:right+1]

        return res
