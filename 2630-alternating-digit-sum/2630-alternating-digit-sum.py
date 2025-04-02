class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0
        n_str = str(n)

        for i in range(len(n_str)):
            num = int(n_str[i])
            if i % 2 == 0:
                sum += num
            else:
                sum -= num
        
        return sum
