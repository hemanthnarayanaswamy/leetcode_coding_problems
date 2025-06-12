class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return ((int(ord(coordinate1[0]) - 96) + int(coordinate1[1])) % 2) == ((int(ord(coordinate2[0]) - 96) + int(coordinate2[1])) % 2)


        