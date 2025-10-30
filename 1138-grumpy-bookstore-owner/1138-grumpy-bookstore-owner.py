class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = 0          # customers already satisfied when not grumpy
        win = 0           # current window gain
        best = 0          # best gain over any window of length minutes
        left = 0

        for right in range(n):
            if grumpy[right] == 0:
                base += customers[right]
            else:
                win += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    win -= customers[left]
                left += 1

            if win > best:
                best = win

        return base + best
