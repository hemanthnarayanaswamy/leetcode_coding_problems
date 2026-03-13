class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        prev = ''
        
        for letter in target:
            for i in alphabets:
                res.append(prev+i)
                if i == letter:
                    break
            prev += letter
            
        return res
