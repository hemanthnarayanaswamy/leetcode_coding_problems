class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        preCount = 0

        for word in words:
            if word[:n] == pref:
                preCount += 1
        
        return preCount