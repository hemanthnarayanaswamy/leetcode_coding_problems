class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        counter = Counter(digitSum(i) for i in range(lowLimit, highLimit + 1))
        return max(counter.values())