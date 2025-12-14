class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        flipr = 0
        flipc = 0
        
        def checkPalindrome(seq):
            flip = 0
            l, r = 0, len(seq)-1
            while l <= r:
                if seq[l] != seq[r]:
                    flip += 1
                l += 1
                r -= 1
            return flip
        
        for row in grid:
            flipr += checkPalindrome(row)
        
        for col in zip(*grid):
            flipc += checkPalindrome(col)
        
        return min(flipr, flipc)
        
