class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        numsFreq = Counter(nums)
        count = 0

        for prefix in set(nums):
            np = len(prefix)
            if np >= len(target):
                continue

            if target.startswith(prefix):
                suffix = target[np:]

                if suffix in numsFreq:
                    y = numsFreq[suffix]
                    x = numsFreq[prefix]

                    if prefix != suffix:
                        count += y * x
                    else: 
                        count += x * (x - 1)
                    
        return count
                    


