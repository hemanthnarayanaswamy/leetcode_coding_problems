class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        numsFreq = Counter(nums)
        n = len(nums)
        f = -1
        x = 0
        count = 0

        for k, v in numsFreq.items():
            if v > f:
                f = v
                x = k
        
        for i in range(n-1):
            if nums[i] == x:
                count += 1
                if count > (i+1)//2 and f - count >= (n - i + 1)//2:
                    return i
            
        return -1

