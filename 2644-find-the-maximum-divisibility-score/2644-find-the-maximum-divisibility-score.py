class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxScore = 0
        res = None

        for d in divisors:
            count = 0
            for num in nums:
                if num % d == 0:
                    count += 1
            
            if count >= maxScore:
                if count > maxScore:
                    maxScore = count
                    res = d
                else:
                    if res:
                        res = min(res, d)
                    else:
                        res = d
        
        return res
