class Solution:
    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = 0

        for left in range(n):
            s = 0
            for right in range(left, n):
                s += nums[right]

                if s % 10 != x:
                    continue

                first = s
                while first >= 10:
                    first //= 10

                if first == x:
                    ans += 1

        return ans