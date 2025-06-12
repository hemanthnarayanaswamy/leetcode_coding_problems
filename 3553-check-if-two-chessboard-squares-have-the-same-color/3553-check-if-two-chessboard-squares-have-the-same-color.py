class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        firstSum = ord(coordinate1[0]) - 96 + int(coordinate1[1])
        secondSum = ord(coordinate2[0]) - 96 + int(coordinate2[1])

        return True if (firstSum % 2 == secondSum % 2) else False


        