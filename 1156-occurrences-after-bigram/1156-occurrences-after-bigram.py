class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textLst = text.split()
        a, b = textLst[0], textLst[1]
        res = []

        for word in textLst[2::]:
            if a == first and b == second:
                res.append(word)
            
            a, b = b, word
        
        return res