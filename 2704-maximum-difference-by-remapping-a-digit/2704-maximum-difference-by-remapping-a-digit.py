class Solution:
    def minMaxDifference(self, num: int) -> int:
        numStr = str(num)
        replace_digit1 = None
        replace_digit2 = None

        for d in numStr:
            if replace_digit1 is None and d != '9':
                replace_digit1 = d
            
            
            if replace_digit2 is None and d != '0':
                replace_digit2 = d
            
            
            if replace_digit1 is not None and replace_digit2 is not None:
                break

        if replace_digit2:
            min_num = int(numStr.replace(replace_digit2, '0'))
        else:
            min_num = num
        
        if replace_digit1:
            max_num = int(numStr.replace(replace_digit1, '9'))
        else:
            max_num = num

        return max_num - min_num