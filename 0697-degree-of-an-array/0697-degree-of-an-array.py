class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            
            right[num] = i
            count[num] = count.get(num, 0) + 1
        
        degree = max(count.values())
        ans = len(nums)

        for x, d in count.items():
            if d == degree:
                ans = min(ans, right[x] - left[x] + 1)
        
        return ans
