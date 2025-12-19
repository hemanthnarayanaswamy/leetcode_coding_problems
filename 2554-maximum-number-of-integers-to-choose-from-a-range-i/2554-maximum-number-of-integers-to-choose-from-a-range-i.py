class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        sum_check = count = 0

        for i in range(1, n+1):
            if i in banned_set:
                continue
            sum_check += i
            if sum_check > maxSum:
                break
            count += 1

        return count
        