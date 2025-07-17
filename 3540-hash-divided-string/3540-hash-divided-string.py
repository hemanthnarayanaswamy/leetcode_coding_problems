class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ords = [ord(i)-97 for i in s]
        res = ""
        for i in range(0, len(ords), k):
            res+= chr((sum(ords[i:i+k])%26)+97)
        return (res)