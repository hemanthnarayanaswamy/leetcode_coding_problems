class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        evenSum = sum(num for num in nums if num % 2 == 0)
        qn = len(queries)
        res = [0] * qn

        for i, query in enumerate(queries):
            val, idx = query

            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
            
            nums[idx] += val 
            if nums[idx] % 2 == 0:
                evenSum += nums[idx]
            
            res[i] = evenSum 
        
        return res



