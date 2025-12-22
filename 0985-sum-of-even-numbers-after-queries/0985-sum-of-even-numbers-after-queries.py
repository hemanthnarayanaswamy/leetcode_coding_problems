class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(num for num in nums if num % 2 == 0)
        res = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            res.append(evenSum)
        
        return res



