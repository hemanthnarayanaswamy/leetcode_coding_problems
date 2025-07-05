class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(2, num+1):
            tempSum = 0
            x = i
            if x < 9:
                tempSum += i 
            else:
                while x > 0:
                    tempSum += x % 10
                    x //= 10
            
            if tempSum % 2 == 0:
                count += 1
        
        return count