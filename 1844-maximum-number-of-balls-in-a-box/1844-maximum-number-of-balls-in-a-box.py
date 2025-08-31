class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        LIMIT = 45  # 1 <= input <= 10 ** 5, implies sum of digits <= 45
        count = [0] * (LIMIT + 1)

        for x in range(lowLimit, highLimit + 1):
            digit_sum = 0
            while x:
                digit_sum += x % 10
                x //= 10
            
            count[digit_sum] += 1
        
        return max(count)