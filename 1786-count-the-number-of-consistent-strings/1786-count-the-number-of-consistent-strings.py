class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed)

        count = len(words)

        for word in words:
            for char in word:
                if char not in set_allowed:
                    count -= 1
                    break 
                    
        return count
        