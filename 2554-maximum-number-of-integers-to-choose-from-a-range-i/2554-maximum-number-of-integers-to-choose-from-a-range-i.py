class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        tmpSum = 0

        for i in range(1, min(n+1, maxSum)):
            if i in banned:
                continue
            
            tmpSum += i
            if tmpSum > maxSum:
                return count
            elif tmpSum == maxSum:
                count += 1
                return count
            else:
                count += 1
        
        return count

