class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = defaultdict(list)
        cols = defaultdict(list)

        A_win = ['x', 'x', 'x']
        B_win = ['o', 'o', 'o']
        
        turn = False

        diagonal = []
        antidiagonal = []

        for r, c in moves:
            play = 'o' if turn else 'x'
            turn = not turn
            rows[r].append(play)
            cols[c].append(play)
            
            if r == c:
                diagonal.append(play)
            
            if r + c == 2:
                antidiagonal.append(play)
        
        for v in rows.values():
            if v == A_win:
                return 'A'
            
            if v == B_win:
                return 'B'
        
        for v in cols.values():
            if v == A_win:
                return 'A'
            
            if v == B_win:
                return 'B'

        if diagonal == A_win:
            return 'A'
        
        if diagonal == B_win:
            return 'B'

        if antidiagonal == A_win:
            return 'A'

        if antidiagonal == B_win:
            return 'B'
        
        for v in rows.values():
            if len(v) < 3:
                return "Pending"
        
        for v in cols.values():
            if len(v) < 3:
                return "Pending"
        
        return 'Draw'


        

