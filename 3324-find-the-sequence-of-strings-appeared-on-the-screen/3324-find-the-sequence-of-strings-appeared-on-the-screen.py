class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        prev = ''
        
        for letter in target:
            start = ord('a')
            end = ord(letter)+1
            for i in range(start, end):
                res.append(prev+chr(i))
            prev += letter
            
        return res
