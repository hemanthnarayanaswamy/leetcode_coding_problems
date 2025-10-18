class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        dnaSequence = {}
        res = []

        if n < 10:
            return res

        for i in range(n - 9):
            dna = s[i:i+10]
            dnaSequence[dna] = dnaSequence.get(dna, 0) + 1
        
        for k, v in dnaSequence.items():
            if v > 1:
                res.append(k)

        return res