class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        A = B = 0
        res  = []

        for s in seq:
            if s == '(':
                if A <= B:
                    A += 1
                    res.append(0)
                else:
                    B += 1
                    res.append(1)
            else:
                if A >= B:
                    A -= 1
                    res.append(0)
                else:
                    B -= 1
                    res.append(1)
        
        return res
