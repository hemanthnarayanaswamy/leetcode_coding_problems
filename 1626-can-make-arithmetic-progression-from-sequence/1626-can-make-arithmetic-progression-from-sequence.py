class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        Ordered = sorted(arr)
        Target = Ordered[1] - Ordered[0]

        Cursor_A = 1
        Cursor_B = 2
        Span = len(Ordered)

        while (Cursor_B < Span):
            
            Value_A = Ordered[Cursor_A]
            Value_B = Ordered[Cursor_B]
            Difference = Value_B - Value_A

            if (Difference == Target):
                Cursor_A += 1
                Cursor_B += 1
            else:
                return False
        
        return True