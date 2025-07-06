class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ''

        s_map = Counter(s)

        for c in s:
            temp = ''
            if c.upper() in s_map and c.lower() in s_map:
                temp = c.upper()
            
            if temp and res:
                if ord(temp) > ord(res):
                    res = temp
            elif temp and not res:
                    res = temp
        
        return res