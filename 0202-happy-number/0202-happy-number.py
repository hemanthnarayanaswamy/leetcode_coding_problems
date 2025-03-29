class Solution:
    def isHappy(self, n: int) -> bool:
        unique_result = set()
        while n not in unique_result:
            unique_result.add(n)
            temp_sum = 0
            for num in str(n):
                temp_sum += int(num)**2
            
            if temp_sum == 1:
                return True
            else:
                n = temp_sum
    
        return False


        