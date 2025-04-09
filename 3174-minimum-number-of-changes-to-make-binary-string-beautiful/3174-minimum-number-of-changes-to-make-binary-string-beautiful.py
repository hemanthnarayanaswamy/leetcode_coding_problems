class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                continue
            changes += 1
        
        return changes
            