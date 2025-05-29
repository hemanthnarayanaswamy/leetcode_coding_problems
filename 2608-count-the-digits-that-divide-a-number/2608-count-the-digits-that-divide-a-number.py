class Solution:
    def countDigits(self, num: int) -> int:
        numList = [int(n) for n in str(num)]
        count = 0

        for n in numList:
            if num % n == 0:
                count += 1
        
        return count