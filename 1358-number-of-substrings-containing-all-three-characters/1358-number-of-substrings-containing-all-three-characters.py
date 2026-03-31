class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0 
        res = 0

        for right, c in enumerate(s):
            freq[c] += 1

            while len(freq) == 3 and freq[s[left]] > 1:
                freq[s[left]] -= 1
                left += 1
            
            if len(freq) == 3:
                res += (left + 1)
            
        return res