class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        
        while len(num_str) > 1:
            temp_sum = 0
            print(temp_sum, num_str)
            for digits in num_str:
                temp_sum += int(digits)   
            num_str = str(temp_sum)
        
        return int(num_str)