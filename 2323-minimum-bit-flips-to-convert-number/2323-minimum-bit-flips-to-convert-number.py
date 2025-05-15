class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == goal:
            return 0

        xor_result = start ^ goal # it return a new number after xor operation

        # the xorResult is int type (Eg: 21, 77, 54 something like this)

        # convert that number to binary that will make it a string and count char 1 and return it or 

        return bin(xor_result).count('1')
        