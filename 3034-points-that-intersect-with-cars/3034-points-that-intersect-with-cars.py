class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums = sorted(nums, key=lambda x: x[0])
        preEnd = 0
        points = 0

        for start, end in nums:
            if start <= preEnd:
                if end > preEnd:
                    points += (end - preEnd)
                else:
                    continue
            else:
                points += (end - start + 1)

            preEnd = end
        
        return points
