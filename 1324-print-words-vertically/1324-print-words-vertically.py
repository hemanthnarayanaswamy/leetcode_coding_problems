class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        matrix = []

        maxLen = 0
        for letter in arr:
            maxLen = max(maxLen, len(letter))
        
        for letter in arr:
            tmp = [w for w in letter]
            tmp.extend([" "]*(maxLen - len(letter)))
            matrix.append(tmp)
        
        res = []
        for ver in zip(*matrix):
            res.append(''.join(ver).rstrip())

        return res

