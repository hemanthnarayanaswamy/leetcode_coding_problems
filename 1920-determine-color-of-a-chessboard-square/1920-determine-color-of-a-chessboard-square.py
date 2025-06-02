class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - 96) % 2 == int(coordinates[1]) % 2:
            return False 
        else:
            return True
