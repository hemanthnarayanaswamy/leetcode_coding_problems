class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
    
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] <= k:
                result.append(nums[i:i+3]) # Append the subarray of three elements
            else:
                return []
        return result
            