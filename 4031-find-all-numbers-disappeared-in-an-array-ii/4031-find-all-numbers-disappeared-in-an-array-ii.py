class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums = set(nums)
        result = []
        start = None

        for number in range(lower, upper + 1):
            if number not in nums:
                if start is None:
                    start = number
            elif start is not None:
                result.append([start, number - 1])
                start = None

        # Handle a missing range that continues through upper
        if start is not None:
            result.append([start, upper])

        return result