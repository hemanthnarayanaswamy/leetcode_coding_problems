class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        result = ''
        flag = True

        for n in numStr:
            temp = n
            if temp == '6' and flag:
                temp = '9'
                flag = False

            result += temp
        
        return int(''.join(result))