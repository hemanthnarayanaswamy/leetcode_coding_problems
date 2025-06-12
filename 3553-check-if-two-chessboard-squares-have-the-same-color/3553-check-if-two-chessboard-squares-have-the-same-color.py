class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        return (alphabet[coordinate1[0]] + int(coordinate1[1])) % 2 == (alphabet[coordinate2[0]] + int(coordinate2[1])) % 2


        