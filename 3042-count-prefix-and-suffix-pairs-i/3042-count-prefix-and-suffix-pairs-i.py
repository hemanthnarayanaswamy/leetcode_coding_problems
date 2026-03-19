class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n = len(str1)

            if str2[:n] == str1 and str2[-n:] == str1:
                return True

        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res