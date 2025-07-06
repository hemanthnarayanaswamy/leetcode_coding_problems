class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = ''
        s_map = Counter(s)

        for i in alphabets:
            temp = ''
            if i in s_map and i.upper() in s_map:
                temp = i.upper()
            
            if temp:
                resVal = ord(res) if res else 0
                tempVal = ord(temp) 
                
                if tempVal > resVal:
                    res = temp
        
        return res


