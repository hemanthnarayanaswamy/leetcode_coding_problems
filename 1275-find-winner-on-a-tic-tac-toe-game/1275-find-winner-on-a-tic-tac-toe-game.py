class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0
        
        for i, (r, c) in enumerate(moves):
            val = 1 if i % 2 else -1
            
            rows[r] += val
            cols[c] += val
            
            if r == c:
                diag += val
            if r + c == 2:
                anti_diag += val
                
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(anti_diag) == 3:
                return "A" if val == -1 else "B"
                
        return "Draw" if len(moves) == 9 else "Pending"