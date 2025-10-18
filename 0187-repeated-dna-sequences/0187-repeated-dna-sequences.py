class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        seen = set()
        dup = set()

        for i in range(n - 9):
            sub = s[i:i+10]
            if sub in seen:
                dup.add(sub)
            else:
                seen.add(sub)
                
        return list(dup)