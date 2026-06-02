class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        subarr = Counter(nums[0:k])
        left = 0
        total = sum(nums[0:k])

        if len(subarr) == k:
            maxSum = sum(subarr)
        else:
            maxSum = 0

        for right in range(k, len(nums)):
            subarr[nums[left]] -= 1
            if subarr[nums[left]] <= 0:
                del subarr[nums[left]]
            total -= nums[left]
            left += 1
            subarr[nums[right]] += 1
            total += nums[right]

            if len(subarr) == k:
                maxSum = max(maxSum, total)
        
        return maxSum
            
