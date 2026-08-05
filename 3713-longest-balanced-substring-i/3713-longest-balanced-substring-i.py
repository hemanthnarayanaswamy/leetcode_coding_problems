class Solution:
    def longestBalanced(self, s: str) -> int:
        longest = 0
        n = len(s)

        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1

                if len(set(freq.values())) == 1:
                    longest = max(longest, j - i + 1)
        
        return longest
