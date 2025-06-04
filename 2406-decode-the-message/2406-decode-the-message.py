class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        subTable = {}
        i = 97

        for char in key:
            if char == " " or char in subTable:
                continue
            
            subTable[char] = chr(i)
            i += 1
        
        decodemessage = []

        for letter in message:
            if letter == " ":
                decodemessage.append(" ")
            else:
                decodemessage.append(subTable[letter])
        
        return ''.join(decodemessage)