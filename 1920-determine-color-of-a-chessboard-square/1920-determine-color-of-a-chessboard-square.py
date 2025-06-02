class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return not (ord(coordinates[0]) - 96) % 2 == int(coordinates[1]) % 2