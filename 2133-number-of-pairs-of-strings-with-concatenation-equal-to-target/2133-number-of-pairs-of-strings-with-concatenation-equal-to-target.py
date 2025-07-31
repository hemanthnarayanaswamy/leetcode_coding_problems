class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        numsFreq = Counter(nums)
        count = 0

        for s in set(nums):
            if target.startswith(s):
                if target[len(s):] in numsFreq:
                    n = numsFreq.get(target[len(s):])
                    x = numsFreq.get(s)
                    if s != target[len(s):]:
                        count += n * x
                    else: 
                        count += n * (n-1)
                    
        return count
                    


