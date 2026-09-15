class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        if sum > 9 * num:
            return res
        
        score = 0

        for _ in range(num):
            if sum >= 9:
                d = 9
            else:
                d = sum

            score += (d * d)
            res += str(d)
            sum -= d

            if sum == 0:
                break
        
        res += '0'*(num - len(res))
        return res
            
