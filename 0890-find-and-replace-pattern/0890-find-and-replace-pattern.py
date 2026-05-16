class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        np = len(pattern)
        res = []

        for word in words:
            if len(word) != np:
                continue
            dict_w = {}
            dict_p = {}
            success = True

            for i in range(np):
                if word[i] in dict_w and dict_w[word[i]] != pattern[i]:
                    success = False
                    break
                
                if pattern[i] in dict_p and dict_p[pattern[i]] != word[i]:
                    success = False
                    break
                
                dict_w[word[i]] = pattern[i]
                dict_p[pattern[i]] = word[i]
            
            if success:
                res.append(word)
            
        return res
