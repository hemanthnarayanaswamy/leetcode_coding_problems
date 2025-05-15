class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        return len([word for word in words if word[:n] == pref])