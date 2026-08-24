class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums = set(nums)
        present = set()

        for i in range(lower, upper+1):
            if i in nums:
                present.add(i)
        
        res = []
        start = lower

        while start in present and start <= upper:
            start += 1

        end = start

        while end <= upper:
            while end not in present and end <= upper:
                end += 1
            else:
                res.append([start, end-1])
                start = end
                while start in present and start <= upper:
                    start += 1
                end = start
        
        return res
