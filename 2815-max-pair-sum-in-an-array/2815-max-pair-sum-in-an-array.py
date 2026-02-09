class Solution:
    def maxSum(self, nums: List[int]) -> int:
        numsMap = defaultdict(list)
        res = -1
        # def maxDigit(num):
        #     d = 0
        #     while num:
        #         q, r = divmod(num, 10)
        #         d = max(d, r)
        #         num = q
        #     return d
        
        for num in nums:
            # d = maxDigit(num)
            d = max(int(n) for n in str(num))
            numsMap[d].append(num)
        
        for _, numList in numsMap.items():
            if len(numList) >= 2:
                numList.sort()
                res = max(res, sum(numList[-2:]))
        
        return res
