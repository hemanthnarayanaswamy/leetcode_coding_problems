class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        nums_freq = Counter(nums)  
        count = 0
        target_len = len(target)   

        for prefix in set(nums):
            prefix_len = len(prefix)
            if prefix_len >= target_len:
                continue

            if target.startswith(prefix):
                suffix = target[prefix_len:]

                if suffix in nums_freq:
                    suffix_count = nums_freq[suffix]
                    prefix_count = nums_freq[prefix]

                    if prefix != suffix:
                        count += suffix_count * prefix_count
                    else: 
                        count += prefix_count * (prefix_count - 1)
                    
        return count