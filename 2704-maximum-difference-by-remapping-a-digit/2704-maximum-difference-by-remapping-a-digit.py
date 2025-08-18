class Solution:
    def minMaxDifference(self, num: int) -> int:
        numStr = str(num)
        replace_digit1 = replace_digit2 = None
        
        for d in numStr:
            if replace_digit1 is None and d != '9':
                replace_digit1 = d
            if replace_digit2 is None and d != '0':
                replace_digit2 = d
            if replace_digit1 and replace_digit2:  
                break
        
        max_num = int(numStr.replace(replace_digit1, '9')) if replace_digit1 else num
        min_num = int(numStr.replace(replace_digit2, '0')) if replace_digit2 else num
        
        return max_num - min_num