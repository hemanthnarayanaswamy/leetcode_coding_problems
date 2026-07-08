class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        maxlen = 0

        for right in range(len(s)):
            c = s[right]
            freq[c] += 1

            while freq[c] > 2:
                freq[s[left]] -= 1
                left += 1
            
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen