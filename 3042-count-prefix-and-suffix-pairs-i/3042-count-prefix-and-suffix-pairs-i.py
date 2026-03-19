class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n = len(str1)
            return str2[:n] == str1 and str2[-n:] == str1

        res = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                str1, str2 = words[i], words[j]
                if len(str1) > len(str2):
                    continue

                if isPrefixAndSuffix(str1, str2):
                    res += 1
        
        return res