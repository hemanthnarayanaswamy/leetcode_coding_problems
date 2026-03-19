class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = res = 0
        preFreq = defaultdict(int)

        for num in nums:
            pre += num

            if pre == k:
                res += 1
            
            res += preFreq[pre - k]
            preFreq[pre] += 1
        
        return res