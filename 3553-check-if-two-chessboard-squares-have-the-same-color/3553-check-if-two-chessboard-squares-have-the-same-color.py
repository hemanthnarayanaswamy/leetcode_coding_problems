class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        one = ord(c1[0]) + int(c1[1])
        two = ord(c2[0]) + int(c2[1])
        return one % 2 == two % 2