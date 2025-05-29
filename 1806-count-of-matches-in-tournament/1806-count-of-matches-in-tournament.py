class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while n > 1:
            advanceTeam = 0
            if n % 2 == 0:
                advanceTeam = n // 2
                n = advanceTeam
            else:
                advanceTeam = (n-1) // 2
                n = advanceTeam + 1
            
            matches += advanceTeam
            print(n, matches)
        
        return matches