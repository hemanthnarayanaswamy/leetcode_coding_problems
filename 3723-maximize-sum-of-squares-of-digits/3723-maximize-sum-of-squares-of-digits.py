class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        if sum > 9 * num:
            return res
        
        for i in range(num):
            if sum >= 9:
                d = 9
            else:
                d = sum

            res += str(d)
            sum -= d

            if sum == 0:
                break
        
        res += '0'*(num - i - 1)
        return res
            
