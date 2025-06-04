class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        result = []
        flag = True

        for n in numStr:
            if n == '6' and flag:
                result.append('9')
                flag = False
            else:
                result.append(n)
        
        return int(''.join(result))