class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        moves = 0

        while target != startValue:
            if target < startValue:
                moves += startValue - target
                break
        
            if target % 2 == 0 and target > startValue:
                target //= 2
            else:
                target += 1
            moves += 1

        return moves

