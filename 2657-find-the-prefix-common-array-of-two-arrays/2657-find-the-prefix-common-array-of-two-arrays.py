class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        prefix = 0

        c = []

        for a, b in zip(A, B):
            setA.add(a)
            setB.add(b)

            prefix = len(setA & setB)
            
            c.append(prefix)
        
        return c