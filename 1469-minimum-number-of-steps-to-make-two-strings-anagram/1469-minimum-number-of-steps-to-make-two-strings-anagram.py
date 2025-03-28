class Solution:
    def minSteps(self, s: str, t: str) -> int:
        replacementCount = 0
        
        s = Counter(s)
        t = Counter(t)
        
        for val, count in s.items():
            if t[val] < count:
                replacementCount += count - t[val]
        
        return replacementCount

        