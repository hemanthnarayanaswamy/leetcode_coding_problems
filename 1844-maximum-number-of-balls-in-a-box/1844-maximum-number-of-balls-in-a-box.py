class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        ballBox = {}
        maxBalls = 0

        for i in range(lowLimit, highLimit+1):
            box = digitSum(i)
            ballBox[box] = ballBox.get(box, 0) + 1
            if ballBox[box] > maxBalls:
                maxBalls = ballBox[box]
        
        return maxBalls