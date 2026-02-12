class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxScore = -1
        res = -1
        divisors.sort()

        for d in divisors:
            count = 0
            for num in nums:
                if num % d == 0:
                    count += 1
            
            if count > maxScore:
                maxScore = count
                res = d

        return res
