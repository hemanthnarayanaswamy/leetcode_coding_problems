class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = sum([int(num) for num in str(x)])

        return y if x % y == 0 else -1