class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        subarr = Counter(nums[0:k])
        total = sum(nums[0:k])
        left = 0
        
        maxSum = total if len(subarr) == k else 0
    
        for right in range(k, len(nums)):
            subarr[nums[left]] -= 1
            total -= nums[left]
            if subarr[nums[left]] <= 0:
                del subarr[nums[left]]
            left += 1

            subarr[nums[right]] += 1
            total += nums[right]

            if len(subarr) == k:
                maxSum = max(maxSum, total)
        
        return maxSum
            
