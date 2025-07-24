class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        goatLst = sentence.split()

        for i in range(len(goatLst)):
            if goatLst[i][0] in 'aeiouAEIOU':
                goatLst[i] = goatLst[i] + 'ma' + (i+1) * 'a'
            else:
                goatLst[i] = goatLst[i][1::] + goatLst[i][0] + 'ma' + (i+1) * 'a'

        
        return ' '.join(goatLst)

