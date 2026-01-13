class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        numsFreq = Counter(nums)
        res = 0 

        for num, frq in numsFreq.items():
            if frq % k == 0:
                res += num * frq
            
        return res
