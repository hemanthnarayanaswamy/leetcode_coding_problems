class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans+=1
        return ans