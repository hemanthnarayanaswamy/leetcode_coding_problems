class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        left = 0
        res = count = 0

        for num in nums:
            if num == maxNum:
                count += 1
            
            while count >= k:
                if nums[left] == maxNum:
                    count -= 1
                left += 1
            
            res += left
        
        return res