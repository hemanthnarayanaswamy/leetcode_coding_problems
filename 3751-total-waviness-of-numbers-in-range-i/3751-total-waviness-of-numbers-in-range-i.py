class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculate(num):
            count = 0
            nums = [int(dig) for dig in str(num)]

            for i in range(1, len(nums)-1):
                p,c,n = nums[i-1], nums[i], nums[i+1]

                if p < c > n or p > c < n:
                    count += 1
            return count

        waviness = 0
        for num in range(num1, num2+1):
            if num < 100:
                continue
            waviness += calculate(num)
        
        return waviness