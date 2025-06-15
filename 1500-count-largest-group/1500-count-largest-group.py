class Solution:
    def countLargestGroup(self, n: int) -> int:
        numGroup = {}

        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        for i in range(1, n+1):
            temp = digit_sum(i)
            numGroup[temp] = numGroup.get(temp, 0) + 1
        
        maxSize = max(numGroup.values())
        return list(numGroup.values()).count(maxSize)






