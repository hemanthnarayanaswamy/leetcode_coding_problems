class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        freq = dict(sorted(Counter(s).items()))
        res = mid = ''
        
        for c in freq:
            if freq[c] % 2:
                mid = c
                
            count = freq[c] // 2
            res += c * count
        
        return res + mid + res[::-1]


