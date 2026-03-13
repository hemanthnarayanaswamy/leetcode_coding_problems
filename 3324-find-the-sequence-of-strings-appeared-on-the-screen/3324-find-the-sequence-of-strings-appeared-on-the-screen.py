class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        prev = ''
        
        def subSequence(prev, letter):
            for i in alphabets:
                res.append(prev+i)
                if i == letter:
                    break
        
        for letter in target:
            subSequence(prev, letter)
            prev += letter
            
        return res
