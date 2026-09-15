class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        if sum > 9 * num:
            return res
        
        while sum > 9:
            res += str(9)
            sum -= 9
        
        res += str(sum)
        res += '0'*(num - len(res))

        return res