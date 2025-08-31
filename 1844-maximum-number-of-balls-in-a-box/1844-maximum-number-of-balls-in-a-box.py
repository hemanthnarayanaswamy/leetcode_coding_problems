class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digitSum(num):
            tmp = [int(d) for d in str(num)]
            return sum(tmp)

        ballBox = {}

        for i in range(lowLimit, highLimit+1):
            box = digitSum(i)
            ballBox[box] = ballBox.get(box, 0) + 1
        
        return max(ballBox.values())