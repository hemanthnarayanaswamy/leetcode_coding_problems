class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = ''
        s_map = Counter(s)

        for i in alphabets:
            temp = ''
            if i in s_map and i.upper() in s_map:
                temp = i.upper()
            
            resVal = ord(res) if res else 0
            tempVal = ord(temp) if temp else 0

            if tempVal > resVal:
                res = temp
        
        return res


