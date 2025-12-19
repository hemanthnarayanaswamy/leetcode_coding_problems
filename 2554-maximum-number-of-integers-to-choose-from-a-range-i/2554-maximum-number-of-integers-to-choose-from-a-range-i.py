class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        total = 0
        count = 0

        for x in range(1, n + 1):
            if x in banned_set:
                continue

            if total + x > maxSum:
                break
            total += x
            count += 1
            
        return count