class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        prev = ''
        
        def subSequence(prev, letter):
            tmp = []
            for i in alphabets:
                tmp.append(prev+i)
                if i == letter:
                    break
            return tmp
        
        for letter in target:
            subArr = subSequence(prev, letter)
            prev = subArr[-1]
            res.extend(subArr)
        
        return res
