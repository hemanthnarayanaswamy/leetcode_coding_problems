class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        def helperDividing(num):
            temp = str(num)

            if '0' in temp: # avoid numbers with 0 in it avoid modulo by zero error
                return 

            for n in temp:
                if num % int(n) != 0:
                    return 
            return num

        for num in range(left, right+1):
            res = helperDividing(num)
            if res:
                result.append(res)
        
        return result
