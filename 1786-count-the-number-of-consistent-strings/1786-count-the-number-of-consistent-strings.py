class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed) # To change the Runtime to O(1) for access

        count = len(words)         # We reduce it as we check the words

        for word in words:
            for char in word:
                if char not in set_allowed:
                    count -= 1
                    break 

        return count
        