class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        def helperDividing(num):
            temp = num

            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return
                temp //= 10
            
            return num

        for num in range(left, right+1):
            res = helperDividing(num)
            if res:
                result.append(res)
        
        return result
